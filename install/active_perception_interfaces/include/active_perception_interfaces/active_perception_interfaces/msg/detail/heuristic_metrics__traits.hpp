// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/msg/heuristic_metrics.hpp"


#ifndef ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__TRAITS_HPP_
#define ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "active_perception_interfaces/msg/detail/heuristic_metrics__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace active_perception_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const HeuristicMetrics & msg,
  std::ostream & out)
{
  out << "{";
  // member: sharpness_score
  {
    out << "sharpness_score: ";
    rosidl_generator_traits::value_to_yaml(msg.sharpness_score, out);
    out << ", ";
  }

  // member: illumination_score
  {
    out << "illumination_score: ";
    rosidl_generator_traits::value_to_yaml(msg.illumination_score, out);
    out << ", ";
  }

  // member: bbox_area_ratio
  {
    out << "bbox_area_ratio: ";
    rosidl_generator_traits::value_to_yaml(msg.bbox_area_ratio, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const HeuristicMetrics & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sharpness_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sharpness_score: ";
    rosidl_generator_traits::value_to_yaml(msg.sharpness_score, out);
    out << "\n";
  }

  // member: illumination_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "illumination_score: ";
    rosidl_generator_traits::value_to_yaml(msg.illumination_score, out);
    out << "\n";
  }

  // member: bbox_area_ratio
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "bbox_area_ratio: ";
    rosidl_generator_traits::value_to_yaml(msg.bbox_area_ratio, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const HeuristicMetrics & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace active_perception_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use active_perception_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const active_perception_interfaces::msg::HeuristicMetrics & msg,
  std::ostream & out, size_t indentation = 0)
{
  active_perception_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use active_perception_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const active_perception_interfaces::msg::HeuristicMetrics & msg)
{
  return active_perception_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<active_perception_interfaces::msg::HeuristicMetrics>()
{
  return "active_perception_interfaces::msg::HeuristicMetrics";
}

template<>
inline const char * name<active_perception_interfaces::msg::HeuristicMetrics>()
{
  return "active_perception_interfaces/msg/HeuristicMetrics";
}

template<>
struct has_fixed_size<active_perception_interfaces::msg::HeuristicMetrics>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<active_perception_interfaces::msg::HeuristicMetrics>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<active_perception_interfaces::msg::HeuristicMetrics>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__TRAITS_HPP_
