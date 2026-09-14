// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/msg/heuristic_metrics.h"


#ifndef ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__STRUCT_H_
#define ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/HeuristicMetrics in the package active_perception_interfaces.
typedef struct active_perception_interfaces__msg__HeuristicMetrics
{
  float sharpness_score;
  float illumination_score;
  float bbox_area_ratio;
} active_perception_interfaces__msg__HeuristicMetrics;

// Struct for a sequence of active_perception_interfaces__msg__HeuristicMetrics.
typedef struct active_perception_interfaces__msg__HeuristicMetrics__Sequence
{
  active_perception_interfaces__msg__HeuristicMetrics * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} active_perception_interfaces__msg__HeuristicMetrics__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__STRUCT_H_
