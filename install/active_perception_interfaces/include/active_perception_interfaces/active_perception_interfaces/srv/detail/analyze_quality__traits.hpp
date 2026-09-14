// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from active_perception_interfaces:srv/AnalyzeQuality.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/srv/analyze_quality.hpp"


#ifndef ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__TRAITS_HPP_
#define ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "active_perception_interfaces/srv/detail/analyze_quality__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__traits.hpp"

namespace active_perception_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AnalyzeQuality_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: image
  {
    out << "image: ";
    to_flow_style_yaml(msg.image, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnalyzeQuality_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: image
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "image:\n";
    to_block_style_yaml(msg.image, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnalyzeQuality_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace active_perception_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use active_perception_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const active_perception_interfaces::srv::AnalyzeQuality_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  active_perception_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use active_perception_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const active_perception_interfaces::srv::AnalyzeQuality_Request & msg)
{
  return active_perception_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<active_perception_interfaces::srv::AnalyzeQuality_Request>()
{
  return "active_perception_interfaces::srv::AnalyzeQuality_Request";
}

template<>
inline const char * name<active_perception_interfaces::srv::AnalyzeQuality_Request>()
{
  return "active_perception_interfaces/srv/AnalyzeQuality_Request";
}

template<>
struct has_fixed_size<active_perception_interfaces::srv::AnalyzeQuality_Request>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Image>::value> {};

template<>
struct has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Request>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Image>::value> {};

template<>
struct is_message<active_perception_interfaces::srv::AnalyzeQuality_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace active_perception_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AnalyzeQuality_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: occlusion_score
  {
    out << "occlusion_score: ";
    rosidl_generator_traits::value_to_yaml(msg.occlusion_score, out);
    out << ", ";
  }

  // member: framing_score
  {
    out << "framing_score: ";
    rosidl_generator_traits::value_to_yaml(msg.framing_score, out);
    out << ", ";
  }

  // member: reasoning
  {
    out << "reasoning: ";
    rosidl_generator_traits::value_to_yaml(msg.reasoning, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnalyzeQuality_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: occlusion_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "occlusion_score: ";
    rosidl_generator_traits::value_to_yaml(msg.occlusion_score, out);
    out << "\n";
  }

  // member: framing_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "framing_score: ";
    rosidl_generator_traits::value_to_yaml(msg.framing_score, out);
    out << "\n";
  }

  // member: reasoning
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reasoning: ";
    rosidl_generator_traits::value_to_yaml(msg.reasoning, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnalyzeQuality_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace active_perception_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use active_perception_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const active_perception_interfaces::srv::AnalyzeQuality_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  active_perception_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use active_perception_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const active_perception_interfaces::srv::AnalyzeQuality_Response & msg)
{
  return active_perception_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<active_perception_interfaces::srv::AnalyzeQuality_Response>()
{
  return "active_perception_interfaces::srv::AnalyzeQuality_Response";
}

template<>
inline const char * name<active_perception_interfaces::srv::AnalyzeQuality_Response>()
{
  return "active_perception_interfaces/srv/AnalyzeQuality_Response";
}

template<>
struct has_fixed_size<active_perception_interfaces::srv::AnalyzeQuality_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<active_perception_interfaces::srv::AnalyzeQuality_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace active_perception_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AnalyzeQuality_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AnalyzeQuality_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AnalyzeQuality_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace active_perception_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use active_perception_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const active_perception_interfaces::srv::AnalyzeQuality_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  active_perception_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use active_perception_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const active_perception_interfaces::srv::AnalyzeQuality_Event & msg)
{
  return active_perception_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<active_perception_interfaces::srv::AnalyzeQuality_Event>()
{
  return "active_perception_interfaces::srv::AnalyzeQuality_Event";
}

template<>
inline const char * name<active_perception_interfaces::srv::AnalyzeQuality_Event>()
{
  return "active_perception_interfaces/srv/AnalyzeQuality_Event";
}

template<>
struct has_fixed_size<active_perception_interfaces::srv::AnalyzeQuality_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Event>
  : std::integral_constant<bool, has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Request>::value && has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<active_perception_interfaces::srv::AnalyzeQuality_Event>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<active_perception_interfaces::srv::AnalyzeQuality>()
{
  return "active_perception_interfaces::srv::AnalyzeQuality";
}

template<>
inline const char * name<active_perception_interfaces::srv::AnalyzeQuality>()
{
  return "active_perception_interfaces/srv/AnalyzeQuality";
}

template<>
struct has_fixed_size<active_perception_interfaces::srv::AnalyzeQuality>
  : std::integral_constant<
    bool,
    has_fixed_size<active_perception_interfaces::srv::AnalyzeQuality_Request>::value &&
    has_fixed_size<active_perception_interfaces::srv::AnalyzeQuality_Response>::value
  >
{
};

template<>
struct has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality>
  : std::integral_constant<
    bool,
    has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Request>::value &&
    has_bounded_size<active_perception_interfaces::srv::AnalyzeQuality_Response>::value
  >
{
};

template<>
struct is_service<active_perception_interfaces::srv::AnalyzeQuality>
  : std::true_type
{
};

template<>
struct is_service_request<active_perception_interfaces::srv::AnalyzeQuality_Request>
  : std::true_type
{
};

template<>
struct is_service_response<active_perception_interfaces::srv::AnalyzeQuality_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__TRAITS_HPP_
