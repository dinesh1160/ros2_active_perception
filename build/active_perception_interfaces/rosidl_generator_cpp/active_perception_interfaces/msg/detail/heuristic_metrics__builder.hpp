// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/msg/heuristic_metrics.hpp"


#ifndef ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__BUILDER_HPP_
#define ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "active_perception_interfaces/msg/detail/heuristic_metrics__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace active_perception_interfaces
{

namespace msg
{

namespace builder
{

class Init_HeuristicMetrics_bbox_area_ratio
{
public:
  explicit Init_HeuristicMetrics_bbox_area_ratio(::active_perception_interfaces::msg::HeuristicMetrics & msg)
  : msg_(msg)
  {}
  ::active_perception_interfaces::msg::HeuristicMetrics bbox_area_ratio(::active_perception_interfaces::msg::HeuristicMetrics::_bbox_area_ratio_type arg)
  {
    msg_.bbox_area_ratio = std::move(arg);
    return std::move(msg_);
  }

private:
  ::active_perception_interfaces::msg::HeuristicMetrics msg_;
};

class Init_HeuristicMetrics_illumination_score
{
public:
  explicit Init_HeuristicMetrics_illumination_score(::active_perception_interfaces::msg::HeuristicMetrics & msg)
  : msg_(msg)
  {}
  Init_HeuristicMetrics_bbox_area_ratio illumination_score(::active_perception_interfaces::msg::HeuristicMetrics::_illumination_score_type arg)
  {
    msg_.illumination_score = std::move(arg);
    return Init_HeuristicMetrics_bbox_area_ratio(msg_);
  }

private:
  ::active_perception_interfaces::msg::HeuristicMetrics msg_;
};

class Init_HeuristicMetrics_sharpness_score
{
public:
  Init_HeuristicMetrics_sharpness_score()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HeuristicMetrics_illumination_score sharpness_score(::active_perception_interfaces::msg::HeuristicMetrics::_sharpness_score_type arg)
  {
    msg_.sharpness_score = std::move(arg);
    return Init_HeuristicMetrics_illumination_score(msg_);
  }

private:
  ::active_perception_interfaces::msg::HeuristicMetrics msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::active_perception_interfaces::msg::HeuristicMetrics>()
{
  return active_perception_interfaces::msg::builder::Init_HeuristicMetrics_sharpness_score();
}

}  // namespace active_perception_interfaces

#endif  // ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__BUILDER_HPP_
