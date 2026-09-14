// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__functions.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace active_perception_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void HeuristicMetrics_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) active_perception_interfaces::msg::HeuristicMetrics(_init);
}

void HeuristicMetrics_fini_function(void * message_memory)
{
  auto typed_message = static_cast<active_perception_interfaces::msg::HeuristicMetrics *>(message_memory);
  typed_message->~HeuristicMetrics();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember HeuristicMetrics_message_member_array[3] = {
  {
    "sharpness_score",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(active_perception_interfaces::msg::HeuristicMetrics, sharpness_score),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "illumination_score",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(active_perception_interfaces::msg::HeuristicMetrics, illumination_score),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "bbox_area_ratio",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(active_perception_interfaces::msg::HeuristicMetrics, bbox_area_ratio),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers HeuristicMetrics_message_members = {
  "active_perception_interfaces::msg",  // message namespace
  "HeuristicMetrics",  // message name
  3,  // number of fields
  sizeof(active_perception_interfaces::msg::HeuristicMetrics),
  false,  // has_any_key_member_
  HeuristicMetrics_message_member_array,  // message members
  HeuristicMetrics_init_function,  // function to initialize message memory (memory has to be allocated)
  HeuristicMetrics_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t HeuristicMetrics_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &HeuristicMetrics_message_members,
  get_message_typesupport_handle_function,
  &active_perception_interfaces__msg__HeuristicMetrics__get_type_hash,
  &active_perception_interfaces__msg__HeuristicMetrics__get_type_description,
  &active_perception_interfaces__msg__HeuristicMetrics__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace active_perception_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<active_perception_interfaces::msg::HeuristicMetrics>()
{
  return &::active_perception_interfaces::msg::rosidl_typesupport_introspection_cpp::HeuristicMetrics_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, active_perception_interfaces, msg, HeuristicMetrics)() {
  return &::active_perception_interfaces::msg::rosidl_typesupport_introspection_cpp::HeuristicMetrics_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
