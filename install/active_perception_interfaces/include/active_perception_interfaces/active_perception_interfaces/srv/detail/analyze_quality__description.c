// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from active_perception_interfaces:srv/AnalyzeQuality.idl
// generated code does not contain a copyright notice

#include "active_perception_interfaces/srv/detail/analyze_quality__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_active_perception_interfaces
const rosidl_type_hash_t *
active_perception_interfaces__srv__AnalyzeQuality__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x69, 0x86, 0x65, 0xeb, 0x72, 0x22, 0x5b, 0xc5,
      0xac, 0xb5, 0x03, 0x2c, 0x9c, 0xb4, 0x72, 0x2d,
      0x62, 0x5f, 0x41, 0x33, 0x82, 0x7e, 0xe8, 0x11,
      0x29, 0x1a, 0x3f, 0xb2, 0x26, 0x87, 0xd7, 0x5b,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_active_perception_interfaces
const rosidl_type_hash_t *
active_perception_interfaces__srv__AnalyzeQuality_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x05, 0x5e, 0x89, 0xc4, 0xe8, 0x2f, 0x0d, 0x50,
      0x57, 0xdf, 0x0b, 0x45, 0xde, 0x11, 0x61, 0x08,
      0xd2, 0x69, 0x72, 0x4e, 0xdc, 0x2f, 0xcf, 0x75,
      0x04, 0xa4, 0xde, 0xfa, 0x00, 0xdc, 0x13, 0xe8,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_active_perception_interfaces
const rosidl_type_hash_t *
active_perception_interfaces__srv__AnalyzeQuality_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x77, 0xdd, 0x6f, 0xf6, 0x2f, 0x46, 0x22, 0x7d,
      0x2d, 0x3b, 0x6c, 0xdc, 0x48, 0xa1, 0xf8, 0x54,
      0x41, 0x29, 0xf6, 0x8c, 0x53, 0xf0, 0xaa, 0xcd,
      0x46, 0xcf, 0x2a, 0xa3, 0x01, 0xbb, 0x15, 0x52,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_active_perception_interfaces
const rosidl_type_hash_t *
active_perception_interfaces__srv__AnalyzeQuality_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf0, 0x39, 0x32, 0xb8, 0x75, 0x24, 0x35, 0xca,
      0x7a, 0x2d, 0xaa, 0x54, 0x24, 0x0f, 0x1e, 0x3f,
      0x53, 0x6f, 0xb6, 0x58, 0xbb, 0xe9, 0x62, 0x0a,
      0x90, 0x43, 0x8c, 0x98, 0x50, 0xd5, 0xf3, 0xf6,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "service_msgs/msg/detail/service_event_info__functions.h"
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "std_msgs/msg/detail/header__functions.h"
#include "sensor_msgs/msg/detail/image__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t sensor_msgs__msg__Image__EXPECTED_HASH = {1, {
    0xd3, 0x1d, 0x41, 0xa9, 0xa4, 0xc4, 0xbc, 0x8e,
    0xae, 0x9b, 0xe7, 0x57, 0xb0, 0xbe, 0xed, 0x30,
    0x65, 0x64, 0xf7, 0x52, 0x6c, 0x88, 0xea, 0x6a,
    0x45, 0x88, 0xfb, 0x95, 0x82, 0x52, 0x7d, 0x47,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
static const rosidl_type_hash_t std_msgs__msg__Header__EXPECTED_HASH = {1, {
    0xf4, 0x9f, 0xb3, 0xae, 0x2c, 0xf0, 0x70, 0xf7,
    0x93, 0x64, 0x5f, 0xf7, 0x49, 0x68, 0x3a, 0xc6,
    0xb0, 0x62, 0x03, 0xe4, 0x1c, 0x89, 0x1e, 0x17,
    0x70, 0x1b, 0x1c, 0xb5, 0x97, 0xce, 0x6a, 0x01,
  }};
#endif

static char active_perception_interfaces__srv__AnalyzeQuality__TYPE_NAME[] = "active_perception_interfaces/srv/AnalyzeQuality";
static char active_perception_interfaces__srv__AnalyzeQuality_Event__TYPE_NAME[] = "active_perception_interfaces/srv/AnalyzeQuality_Event";
static char active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME[] = "active_perception_interfaces/srv/AnalyzeQuality_Request";
static char active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME[] = "active_perception_interfaces/srv/AnalyzeQuality_Response";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char sensor_msgs__msg__Image__TYPE_NAME[] = "sensor_msgs/msg/Image";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";
static char std_msgs__msg__Header__TYPE_NAME[] = "std_msgs/msg/Header";

// Define type names, field names, and default values
static char active_perception_interfaces__srv__AnalyzeQuality__FIELD_NAME__request_message[] = "request_message";
static char active_perception_interfaces__srv__AnalyzeQuality__FIELD_NAME__response_message[] = "response_message";
static char active_perception_interfaces__srv__AnalyzeQuality__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field active_perception_interfaces__srv__AnalyzeQuality__FIELDS[] = {
  {
    {active_perception_interfaces__srv__AnalyzeQuality__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME, 55, 55},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME, 56, 56},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {active_perception_interfaces__srv__AnalyzeQuality_Event__TYPE_NAME, 53, 53},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription active_perception_interfaces__srv__AnalyzeQuality__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Event__TYPE_NAME, 53, 53},
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME, 55, 55},
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME, 56, 56},
    {NULL, 0, 0},
  },
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {sensor_msgs__msg__Image__TYPE_NAME, 21, 21},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
active_perception_interfaces__srv__AnalyzeQuality__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {active_perception_interfaces__srv__AnalyzeQuality__TYPE_NAME, 47, 47},
      {active_perception_interfaces__srv__AnalyzeQuality__FIELDS, 3, 3},
    },
    {active_perception_interfaces__srv__AnalyzeQuality__REFERENCED_TYPE_DESCRIPTIONS, 7, 7},
  };
  if (!constructed) {
    description.referenced_type_descriptions.data[0].fields = active_perception_interfaces__srv__AnalyzeQuality_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = active_perception_interfaces__srv__AnalyzeQuality_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[2].fields = active_perception_interfaces__srv__AnalyzeQuality_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&sensor_msgs__msg__Image__EXPECTED_HASH, sensor_msgs__msg__Image__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = sensor_msgs__msg__Image__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[5].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[6].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char active_perception_interfaces__srv__AnalyzeQuality_Request__FIELD_NAME__image[] = "image";

static rosidl_runtime_c__type_description__Field active_perception_interfaces__srv__AnalyzeQuality_Request__FIELDS[] = {
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Request__FIELD_NAME__image, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {sensor_msgs__msg__Image__TYPE_NAME, 21, 21},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription active_perception_interfaces__srv__AnalyzeQuality_Request__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {sensor_msgs__msg__Image__TYPE_NAME, 21, 21},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
active_perception_interfaces__srv__AnalyzeQuality_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME, 55, 55},
      {active_perception_interfaces__srv__AnalyzeQuality_Request__FIELDS, 1, 1},
    },
    {active_perception_interfaces__srv__AnalyzeQuality_Request__REFERENCED_TYPE_DESCRIPTIONS, 3, 3},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&sensor_msgs__msg__Image__EXPECTED_HASH, sensor_msgs__msg__Image__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = sensor_msgs__msg__Image__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char active_perception_interfaces__srv__AnalyzeQuality_Response__FIELD_NAME__occlusion_score[] = "occlusion_score";
static char active_perception_interfaces__srv__AnalyzeQuality_Response__FIELD_NAME__framing_score[] = "framing_score";
static char active_perception_interfaces__srv__AnalyzeQuality_Response__FIELD_NAME__reasoning[] = "reasoning";

static rosidl_runtime_c__type_description__Field active_perception_interfaces__srv__AnalyzeQuality_Response__FIELDS[] = {
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Response__FIELD_NAME__occlusion_score, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Response__FIELD_NAME__framing_score, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Response__FIELD_NAME__reasoning, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
active_perception_interfaces__srv__AnalyzeQuality_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME, 56, 56},
      {active_perception_interfaces__srv__AnalyzeQuality_Response__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char active_perception_interfaces__srv__AnalyzeQuality_Event__FIELD_NAME__info[] = "info";
static char active_perception_interfaces__srv__AnalyzeQuality_Event__FIELD_NAME__request[] = "request";
static char active_perception_interfaces__srv__AnalyzeQuality_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field active_perception_interfaces__srv__AnalyzeQuality_Event__FIELDS[] = {
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME, 55, 55},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME, 56, 56},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription active_perception_interfaces__srv__AnalyzeQuality_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME, 55, 55},
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME, 56, 56},
    {NULL, 0, 0},
  },
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {sensor_msgs__msg__Image__TYPE_NAME, 21, 21},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
  {
    {std_msgs__msg__Header__TYPE_NAME, 19, 19},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
active_perception_interfaces__srv__AnalyzeQuality_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {active_perception_interfaces__srv__AnalyzeQuality_Event__TYPE_NAME, 53, 53},
      {active_perception_interfaces__srv__AnalyzeQuality_Event__FIELDS, 3, 3},
    },
    {active_perception_interfaces__srv__AnalyzeQuality_Event__REFERENCED_TYPE_DESCRIPTIONS, 6, 6},
  };
  if (!constructed) {
    description.referenced_type_descriptions.data[0].fields = active_perception_interfaces__srv__AnalyzeQuality_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[1].fields = active_perception_interfaces__srv__AnalyzeQuality_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&sensor_msgs__msg__Image__EXPECTED_HASH, sensor_msgs__msg__Image__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[3].fields = sensor_msgs__msg__Image__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[4].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&std_msgs__msg__Header__EXPECTED_HASH, std_msgs__msg__Header__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[5].fields = std_msgs__msg__Header__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "sensor_msgs/Image image\n"
  "---\n"
  "float32 occlusion_score\n"
  "float32 framing_score\n"
  "string reasoning";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
active_perception_interfaces__srv__AnalyzeQuality__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {active_perception_interfaces__srv__AnalyzeQuality__TYPE_NAME, 47, 47},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 91, 91},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
active_perception_interfaces__srv__AnalyzeQuality_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {active_perception_interfaces__srv__AnalyzeQuality_Request__TYPE_NAME, 55, 55},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
active_perception_interfaces__srv__AnalyzeQuality_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {active_perception_interfaces__srv__AnalyzeQuality_Response__TYPE_NAME, 56, 56},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
active_perception_interfaces__srv__AnalyzeQuality_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {active_perception_interfaces__srv__AnalyzeQuality_Event__TYPE_NAME, 53, 53},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
active_perception_interfaces__srv__AnalyzeQuality__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[8];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 8, 8};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *active_perception_interfaces__srv__AnalyzeQuality__get_individual_type_description_source(NULL),
    sources[1] = *active_perception_interfaces__srv__AnalyzeQuality_Event__get_individual_type_description_source(NULL);
    sources[2] = *active_perception_interfaces__srv__AnalyzeQuality_Request__get_individual_type_description_source(NULL);
    sources[3] = *active_perception_interfaces__srv__AnalyzeQuality_Response__get_individual_type_description_source(NULL);
    sources[4] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[5] = *sensor_msgs__msg__Image__get_individual_type_description_source(NULL);
    sources[6] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[7] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
active_perception_interfaces__srv__AnalyzeQuality_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[4];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 4, 4};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *active_perception_interfaces__srv__AnalyzeQuality_Request__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *sensor_msgs__msg__Image__get_individual_type_description_source(NULL);
    sources[3] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
active_perception_interfaces__srv__AnalyzeQuality_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *active_perception_interfaces__srv__AnalyzeQuality_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
active_perception_interfaces__srv__AnalyzeQuality_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[7];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 7, 7};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *active_perception_interfaces__srv__AnalyzeQuality_Event__get_individual_type_description_source(NULL),
    sources[1] = *active_perception_interfaces__srv__AnalyzeQuality_Request__get_individual_type_description_source(NULL);
    sources[2] = *active_perception_interfaces__srv__AnalyzeQuality_Response__get_individual_type_description_source(NULL);
    sources[3] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[4] = *sensor_msgs__msg__Image__get_individual_type_description_source(NULL);
    sources[5] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    sources[6] = *std_msgs__msg__Header__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
