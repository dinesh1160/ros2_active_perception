// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "active_perception_interfaces/msg/detail/heuristic_metrics__rosidl_typesupport_introspection_c.h"
#include "active_perception_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__functions.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  active_perception_interfaces__msg__HeuristicMetrics__init(message_memory);
}

void active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_fini_function(void * message_memory)
{
  active_perception_interfaces__msg__HeuristicMetrics__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_member_array[3] = {
  {
    "sharpness_score",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(active_perception_interfaces__msg__HeuristicMetrics, sharpness_score),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "illumination_score",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(active_perception_interfaces__msg__HeuristicMetrics, illumination_score),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "bbox_area_ratio",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(active_perception_interfaces__msg__HeuristicMetrics, bbox_area_ratio),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_members = {
  "active_perception_interfaces__msg",  // message namespace
  "HeuristicMetrics",  // message name
  3,  // number of fields
  sizeof(active_perception_interfaces__msg__HeuristicMetrics),
  false,  // has_any_key_member_
  active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_member_array,  // message members
  active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_init_function,  // function to initialize message memory (memory has to be allocated)
  active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_type_support_handle = {
  0,
  &active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_members,
  get_message_typesupport_handle_function,
  &active_perception_interfaces__msg__HeuristicMetrics__get_type_hash,
  &active_perception_interfaces__msg__HeuristicMetrics__get_type_description,
  &active_perception_interfaces__msg__HeuristicMetrics__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_active_perception_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, active_perception_interfaces, msg, HeuristicMetrics)() {
  if (!active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_type_support_handle.typesupport_identifier) {
    active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &active_perception_interfaces__msg__HeuristicMetrics__rosidl_typesupport_introspection_c__HeuristicMetrics_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
