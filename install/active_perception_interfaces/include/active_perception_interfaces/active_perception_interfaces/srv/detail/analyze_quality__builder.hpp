// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from active_perception_interfaces:srv/AnalyzeQuality.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/srv/analyze_quality.hpp"


#ifndef ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__BUILDER_HPP_
#define ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "active_perception_interfaces/srv/detail/analyze_quality__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace active_perception_interfaces
{

namespace srv
{

namespace builder
{

class Init_AnalyzeQuality_Request_image
{
public:
  Init_AnalyzeQuality_Request_image()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::active_perception_interfaces::srv::AnalyzeQuality_Request image(::active_perception_interfaces::srv::AnalyzeQuality_Request::_image_type arg)
  {
    msg_.image = std::move(arg);
    return std::move(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::active_perception_interfaces::srv::AnalyzeQuality_Request>()
{
  return active_perception_interfaces::srv::builder::Init_AnalyzeQuality_Request_image();
}

}  // namespace active_perception_interfaces


namespace active_perception_interfaces
{

namespace srv
{

namespace builder
{

class Init_AnalyzeQuality_Response_reasoning
{
public:
  explicit Init_AnalyzeQuality_Response_reasoning(::active_perception_interfaces::srv::AnalyzeQuality_Response & msg)
  : msg_(msg)
  {}
  ::active_perception_interfaces::srv::AnalyzeQuality_Response reasoning(::active_perception_interfaces::srv::AnalyzeQuality_Response::_reasoning_type arg)
  {
    msg_.reasoning = std::move(arg);
    return std::move(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Response msg_;
};

class Init_AnalyzeQuality_Response_framing_score
{
public:
  explicit Init_AnalyzeQuality_Response_framing_score(::active_perception_interfaces::srv::AnalyzeQuality_Response & msg)
  : msg_(msg)
  {}
  Init_AnalyzeQuality_Response_reasoning framing_score(::active_perception_interfaces::srv::AnalyzeQuality_Response::_framing_score_type arg)
  {
    msg_.framing_score = std::move(arg);
    return Init_AnalyzeQuality_Response_reasoning(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Response msg_;
};

class Init_AnalyzeQuality_Response_occlusion_score
{
public:
  Init_AnalyzeQuality_Response_occlusion_score()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnalyzeQuality_Response_framing_score occlusion_score(::active_perception_interfaces::srv::AnalyzeQuality_Response::_occlusion_score_type arg)
  {
    msg_.occlusion_score = std::move(arg);
    return Init_AnalyzeQuality_Response_framing_score(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::active_perception_interfaces::srv::AnalyzeQuality_Response>()
{
  return active_perception_interfaces::srv::builder::Init_AnalyzeQuality_Response_occlusion_score();
}

}  // namespace active_perception_interfaces


namespace active_perception_interfaces
{

namespace srv
{

namespace builder
{

class Init_AnalyzeQuality_Event_response
{
public:
  explicit Init_AnalyzeQuality_Event_response(::active_perception_interfaces::srv::AnalyzeQuality_Event & msg)
  : msg_(msg)
  {}
  ::active_perception_interfaces::srv::AnalyzeQuality_Event response(::active_perception_interfaces::srv::AnalyzeQuality_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Event msg_;
};

class Init_AnalyzeQuality_Event_request
{
public:
  explicit Init_AnalyzeQuality_Event_request(::active_perception_interfaces::srv::AnalyzeQuality_Event & msg)
  : msg_(msg)
  {}
  Init_AnalyzeQuality_Event_response request(::active_perception_interfaces::srv::AnalyzeQuality_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_AnalyzeQuality_Event_response(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Event msg_;
};

class Init_AnalyzeQuality_Event_info
{
public:
  Init_AnalyzeQuality_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AnalyzeQuality_Event_request info(::active_perception_interfaces::srv::AnalyzeQuality_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_AnalyzeQuality_Event_request(msg_);
  }

private:
  ::active_perception_interfaces::srv::AnalyzeQuality_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::active_perception_interfaces::srv::AnalyzeQuality_Event>()
{
  return active_perception_interfaces::srv::builder::Init_AnalyzeQuality_Event_info();
}

}  // namespace active_perception_interfaces

#endif  // ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__BUILDER_HPP_
