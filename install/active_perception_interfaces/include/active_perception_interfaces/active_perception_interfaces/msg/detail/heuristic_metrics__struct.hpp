// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/msg/heuristic_metrics.hpp"


#ifndef ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__STRUCT_HPP_
#define ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__active_perception_interfaces__msg__HeuristicMetrics __attribute__((deprecated))
#else
# define DEPRECATED__active_perception_interfaces__msg__HeuristicMetrics __declspec(deprecated)
#endif

namespace active_perception_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HeuristicMetrics_
{
  using Type = HeuristicMetrics_<ContainerAllocator>;

  explicit HeuristicMetrics_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sharpness_score = 0.0f;
      this->illumination_score = 0.0f;
      this->bbox_area_ratio = 0.0f;
    }
  }

  explicit HeuristicMetrics_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sharpness_score = 0.0f;
      this->illumination_score = 0.0f;
      this->bbox_area_ratio = 0.0f;
    }
  }

  // field types and members
  using _sharpness_score_type =
    float;
  _sharpness_score_type sharpness_score;
  using _illumination_score_type =
    float;
  _illumination_score_type illumination_score;
  using _bbox_area_ratio_type =
    float;
  _bbox_area_ratio_type bbox_area_ratio;

  // setters for named parameter idiom
  Type & set__sharpness_score(
    const float & _arg)
  {
    this->sharpness_score = _arg;
    return *this;
  }
  Type & set__illumination_score(
    const float & _arg)
  {
    this->illumination_score = _arg;
    return *this;
  }
  Type & set__bbox_area_ratio(
    const float & _arg)
  {
    this->bbox_area_ratio = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator> *;
  using ConstRawPtr =
    const active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__active_perception_interfaces__msg__HeuristicMetrics
    std::shared_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__active_perception_interfaces__msg__HeuristicMetrics
    std::shared_ptr<active_perception_interfaces::msg::HeuristicMetrics_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HeuristicMetrics_ & other) const
  {
    if (this->sharpness_score != other.sharpness_score) {
      return false;
    }
    if (this->illumination_score != other.illumination_score) {
      return false;
    }
    if (this->bbox_area_ratio != other.bbox_area_ratio) {
      return false;
    }
    return true;
  }
  bool operator!=(const HeuristicMetrics_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HeuristicMetrics_

// alias to use template instance with default allocator
using HeuristicMetrics =
  active_perception_interfaces::msg::HeuristicMetrics_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace active_perception_interfaces

#endif  // ACTIVE_PERCEPTION_INTERFACES__MSG__DETAIL__HEURISTIC_METRICS__STRUCT_HPP_
