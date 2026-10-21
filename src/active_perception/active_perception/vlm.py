import json
import os


def load_env_file(path: str):
    if not path or not os.path.isfile(path):
        return False
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip().removeprefix('export ').strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)
    return True


def build_prompt(target):
    return (
        f"You are an active perception judge for a rover. Look at the target object ({target}) "
        "in this image. "
        f"1. occlusion_score: Is the {target} blocked by anything? "
        "(Score 0-100, where 100 is fully visible). "
        f"2. framing_score: Is the entire {target} in the frame? "
        "(Score 0-100, where 100 is perfect). "
        "3. reasoning: Provide a 1-sentence explanation of your scores."
    )


class GeminiJudge:
    def __init__(self, api_key, model, timeout_sec=20.0):
        from google import genai
        from google.genai import types

        self.types = types
        self.model = model
        self.client = genai.Client(
            api_key=api_key, http_options=types.HttpOptions(timeout=int(timeout_sec * 1000)))
        self.schema = types.Schema(
            type=types.Type.OBJECT,
            properties={
                'occlusion_score': types.Schema(type=types.Type.NUMBER),
                'framing_score': types.Schema(type=types.Type.NUMBER),
                'reasoning': types.Schema(type=types.Type.STRING),
            },
            required=['occlusion_score', 'framing_score', 'reasoning'],
        )

    def __call__(self, jpeg_bytes, target):
        types = self.types
        response = self.client.models.generate_content(
            model=self.model,
            contents=[types.Part.from_bytes(data=jpeg_bytes, mime_type='image/jpeg'),
                      build_prompt(target)],
            config=types.GenerateContentConfig(
                response_mime_type='application/json', response_schema=self.schema),
        )
        result = json.loads(response.text)
        clamp = lambda v: min(100.0, max(0.0, float(v)))  # noqa: E731
        return (clamp(result['occlusion_score']), clamp(result['framing_score']),
                str(result['reasoning']))
