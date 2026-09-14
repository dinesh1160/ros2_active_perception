// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice
#ifndef ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "active_perception_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
bool cdr_serialize_active_perception_interfaces__msg__HeuristicMetrics(
  const active_perception_interfaces__msg__HeuristicMetrics * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
bool cdr_deserialize_active_perception_interfaces__msg__HeuristicMetrics(
  eprosima::fastcdr::Cdr &,
  active_perception_interfaces__msg__HeuristicMetrics * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
size_t get_serialized_size_active_perception_interfaces__msg__HeuristicMetrics(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
size_t max_serialized_size_active_perception_interfaces__msg__HeuristicMetrics(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
bool cdr_serialize_key_active_perception_interfaces__msg__HeuristicMetrics(
  const active_perception_interfaces__msg__HeuristicMetrics * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
size_t get_serialized_size_key_active_perception_interfaces__msg__HeuristicMetrics(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
size_t max_serialized_size_key_active_perception_interfaces__msg__HeuristicMetrics(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_active_perception_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, active_perception_interfaces, msg, HeuristicMetrics)();

#ifdef __cplusplus
}
#endif

#endif  // ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
