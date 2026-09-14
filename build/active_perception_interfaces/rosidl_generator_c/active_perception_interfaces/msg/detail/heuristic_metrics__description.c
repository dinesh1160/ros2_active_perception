// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

#include "active_perception_interfaces/msg/detail/heuristic_metrics__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_active_perception_interfaces
const rosidl_type_hash_t *
active_perception_interfaces__msg__HeuristicMetrics__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x87, 0x3b, 0x70, 0x54, 0x56, 0x69, 0xbc, 0x9f,
      0x5b, 0xb9, 0xf6, 0xa0, 0xf2, 0xae, 0xf6, 0xec,
      0x8f, 0x31, 0x9d, 0x4e, 0x1d, 0x09, 0x0a, 0x67,
      0x0d, 0x1e, 0x1e, 0x4a, 0x49, 0x58, 0x20, 0x70,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char active_perception_interfaces__msg__HeuristicMetrics__TYPE_NAME[] = "active_perception_interfaces/msg/HeuristicMetrics";

// Define type names, field names, and default values
static char active_perception_interfaces__msg__HeuristicMetrics__FIELD_NAME__sharpness_score[] = "sharpness_score";
static char active_perception_interfaces__msg__HeuristicMetrics__FIELD_NAME__illumination_score[] = "illumination_score";
static char active_perception_interfaces__msg__HeuristicMetrics__FIELD_NAME__bbox_area_ratio[] = "bbox_area_ratio";

static rosidl_runtime_c__type_description__Field active_perception_interfaces__msg__HeuristicMetrics__FIELDS[] = {
  {
    {active_perception_interfaces__msg__HeuristicMetrics__FIELD_NAME__sharpness_score, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__msg__HeuristicMetrics__FIELD_NAME__illumination_score, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {active_perception_interfaces__msg__HeuristicMetrics__FIELD_NAME__bbox_area_ratio, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
active_perception_interfaces__msg__HeuristicMetrics__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {active_perception_interfaces__msg__HeuristicMetrics__TYPE_NAME, 49, 49},
      {active_perception_interfaces__msg__HeuristicMetrics__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float32 sharpness_score\n"
  "float32 illumination_score\n"
  "float32 bbox_area_ratio";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
active_perception_interfaces__msg__HeuristicMetrics__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {active_perception_interfaces__msg__HeuristicMetrics__TYPE_NAME, 49, 49},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 75, 75},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
active_perception_interfaces__msg__HeuristicMetrics__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *active_perception_interfaces__msg__HeuristicMetrics__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
