// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from active_perception_interfaces:srv/AnalyzeQuality.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "active_perception_interfaces/srv/analyze_quality.hpp"


#ifndef ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__STRUCT_HPP_
#define ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'image'
#include "sensor_msgs/msg/detail/image__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Request __attribute__((deprecated))
#else
# define DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Request __declspec(deprecated)
#endif

namespace active_perception_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AnalyzeQuality_Request_
{
  using Type = AnalyzeQuality_Request_<ContainerAllocator>;

  explicit AnalyzeQuality_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : image(_init)
  {
    (void)_init;
  }

  explicit AnalyzeQuality_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : image(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _image_type =
    sensor_msgs::msg::Image_<ContainerAllocator>;
  _image_type image;

  // setters for named parameter idiom
  Type & set__image(
    const sensor_msgs::msg::Image_<ContainerAllocator> & _arg)
  {
    this->image = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Request
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Request
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnalyzeQuality_Request_ & other) const
  {
    if (this->image != other.image) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnalyzeQuality_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnalyzeQuality_Request_

// alias to use template instance with default allocator
using AnalyzeQuality_Request =
  active_perception_interfaces::srv::AnalyzeQuality_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace active_perception_interfaces


#ifndef _WIN32
# define DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Response __attribute__((deprecated))
#else
# define DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Response __declspec(deprecated)
#endif

namespace active_perception_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AnalyzeQuality_Response_
{
  using Type = AnalyzeQuality_Response_<ContainerAllocator>;

  explicit AnalyzeQuality_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->occlusion_score = 0.0f;
      this->framing_score = 0.0f;
      this->reasoning = "";
    }
  }

  explicit AnalyzeQuality_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : reasoning(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->occlusion_score = 0.0f;
      this->framing_score = 0.0f;
      this->reasoning = "";
    }
  }

  // field types and members
  using _occlusion_score_type =
    float;
  _occlusion_score_type occlusion_score;
  using _framing_score_type =
    float;
  _framing_score_type framing_score;
  using _reasoning_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _reasoning_type reasoning;

  // setters for named parameter idiom
  Type & set__occlusion_score(
    const float & _arg)
  {
    this->occlusion_score = _arg;
    return *this;
  }
  Type & set__framing_score(
    const float & _arg)
  {
    this->framing_score = _arg;
    return *this;
  }
  Type & set__reasoning(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->reasoning = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Response
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Response
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnalyzeQuality_Response_ & other) const
  {
    if (this->occlusion_score != other.occlusion_score) {
      return false;
    }
    if (this->framing_score != other.framing_score) {
      return false;
    }
    if (this->reasoning != other.reasoning) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnalyzeQuality_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnalyzeQuality_Response_

// alias to use template instance with default allocator
using AnalyzeQuality_Response =
  active_perception_interfaces::srv::AnalyzeQuality_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace active_perception_interfaces


// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Event __attribute__((deprecated))
#else
# define DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Event __declspec(deprecated)
#endif

namespace active_perception_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AnalyzeQuality_Event_
{
  using Type = AnalyzeQuality_Event_<ContainerAllocator>;

  explicit AnalyzeQuality_Event_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_init)
  {
    (void)_init;
  }

  explicit AnalyzeQuality_Event_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _info_type =
    service_msgs::msg::ServiceEventInfo_<ContainerAllocator>;
  _info_type info;
  using _request_type =
    rosidl_runtime_cpp::BoundedVector<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>>;
  _request_type request;
  using _response_type =
    rosidl_runtime_cpp::BoundedVector<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__info(
    const service_msgs::msg::ServiceEventInfo_<ContainerAllocator> & _arg)
  {
    this->info = _arg;
    return *this;
  }
  Type & set__request(
    const rosidl_runtime_cpp::BoundedVector<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<active_perception_interfaces::srv::AnalyzeQuality_Request_<ContainerAllocator>>> & _arg)
  {
    this->request = _arg;
    return *this;
  }
  Type & set__response(
    const rosidl_runtime_cpp::BoundedVector<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<active_perception_interfaces::srv::AnalyzeQuality_Response_<ContainerAllocator>>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator> *;
  using ConstRawPtr =
    const active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Event
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__active_perception_interfaces__srv__AnalyzeQuality_Event
    std::shared_ptr<active_perception_interfaces::srv::AnalyzeQuality_Event_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AnalyzeQuality_Event_ & other) const
  {
    if (this->info != other.info) {
      return false;
    }
    if (this->request != other.request) {
      return false;
    }
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const AnalyzeQuality_Event_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AnalyzeQuality_Event_

// alias to use template instance with default allocator
using AnalyzeQuality_Event =
  active_perception_interfaces::srv::AnalyzeQuality_Event_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace active_perception_interfaces

namespace active_perception_interfaces
{

namespace srv
{

struct AnalyzeQuality
{
  using Request = active_perception_interfaces::srv::AnalyzeQuality_Request;
  using Response = active_perception_interfaces::srv::AnalyzeQuality_Response;
  using Event = active_perception_interfaces::srv::AnalyzeQuality_Event;
};

}  // namespace srv

}  // namespace active_perception_interfaces

#endif  // ACTIVE_PERCEPTION_INTERFACES__SRV__DETAIL__ANALYZE_QUALITY__STRUCT_HPP_
