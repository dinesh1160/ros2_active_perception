"""Shared helpers for converting sensor_msgs/Image to OpenCV without cv_bridge."""

import cv2
import numpy as np
from sensor_msgs.msg import Image

# encoding -> (channels, cv2 conversion to BGR or None if already BGR)
_ENCODINGS = {
    'bgr8': (3, None),
    'rgb8': (3, cv2.COLOR_RGB2BGR),
    'bgra8': (4, cv2.COLOR_BGRA2BGR),
    'rgba8': (4, cv2.COLOR_RGBA2BGR),
    'mono8': (1, cv2.COLOR_GRAY2BGR),
    '8UC1': (1, cv2.COLOR_GRAY2BGR),
    '8UC3': (3, None),
    'yuv422': (2, cv2.COLOR_YUV2BGR_UYVY),
    'uyvy': (2, cv2.COLOR_YUV2BGR_UYVY),
    'yuv422_yuy2': (2, cv2.COLOR_YUV2BGR_YUY2),
    'yuyv': (2, cv2.COLOR_YUV2BGR_YUY2),
}


def image_msg_to_bgr(msg: Image) -> np.ndarray:
    """Convert a ROS Image to a contiguous BGR uint8 array (h, w, 3).

    Handles row padding (step > width * channels) and the encodings common to
    USB / Pi cameras. Raises ValueError for anything else.
    """
    encoding = msg.encoding.lower() if msg.encoding.lower() in _ENCODINGS else msg.encoding
    if encoding not in _ENCODINGS:
        raise ValueError(f"Unsupported image encoding '{msg.encoding}'")

    channels, conversion = _ENCODINGS[encoding]
    row_bytes = msg.width * channels
    if msg.step < row_bytes or len(msg.data) < msg.step * msg.height:
        raise ValueError(
            f"Image data size mismatch: {msg.width}x{msg.height} {msg.encoding}, "
            f"step={msg.step}, len={len(msg.data)}")

    buf = np.frombuffer(msg.data, dtype=np.uint8, count=msg.step * msg.height)
    # Drop any per-row padding, then restore the channel axis
    img = buf.reshape(msg.height, msg.step)[:, :row_bytes]
    img = img.reshape(msg.height, msg.width, channels) if channels > 1 \
        else img.reshape(msg.height, msg.width)

    if conversion is not None:
        return cv2.cvtColor(img, conversion)
    return np.ascontiguousarray(img)
