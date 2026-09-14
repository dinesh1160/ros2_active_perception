// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from active_perception_interfaces:srv/AnalyzeQuality.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/srv/analyze_quality.h"


#ifndef ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__STRUCT_H_
#define ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.h"

/// Struct defined in srv/AnalyzeQuality in the package active_perception_interfaces.
typedef struct active_perception_interfaces__srv__AnalyzeQuality_Request
{
  sensor_msgs__msg__Image image;
} active_perception_interfaces__srv__AnalyzeQuality_Request;

// Struct for a sequence of active_perception_interfaces__srv__AnalyzeQuality_Request.
typedef struct active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence
{
  active_perception_interfaces__srv__AnalyzeQuality_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'reasoning'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AnalyzeQuality in the package active_perception_interfaces.
typedef struct active_perception_interfaces__srv__AnalyzeQuality_Response
{
  float occlusion_score;
  float framing_score;
  rosidl_runtime_c__String reasoning;
} active_perception_interfaces__srv__AnalyzeQuality_Response;

// Struct for a sequence of active_perception_interfaces__srv__AnalyzeQuality_Response.
typedef struct active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence
{
  active_perception_interfaces__srv__AnalyzeQuality_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  active_perception_interfaces__srv__AnalyzeQuality_Event__request__MAX_SIZE = 1
};
// response
enum
{
  active_perception_interfaces__srv__AnalyzeQuality_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/AnalyzeQuality in the package active_perception_interfaces.
typedef struct active_perception_interfaces__srv__AnalyzeQuality_Event
{
  service_msgs__msg__ServiceEventInfo info;
  active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence request;
  active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence response;
} active_perception_interfaces__srv__AnalyzeQuality_Event;

// Struct for a sequence of active_perception_interfaces__srv__AnalyzeQuality_Event.
typedef struct active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence
{
  active_perception_interfaces__srv__AnalyzeQuality_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__STRUCT_H_
