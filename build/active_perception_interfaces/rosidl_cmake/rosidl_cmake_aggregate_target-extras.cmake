# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target active_perception_interfaces::active_perception_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${active_perception_interfaces_TARGETS}.
if(active_perception_interfaces_TARGETS AND NOT TARGET active_perception_interfaces::active_perception_interfaces)
  add_library(active_perception_interfaces::active_perception_interfaces INTERFACE IMPORTED)
  set_target_properties(active_perception_interfaces::active_perception_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${active_perception_interfaces_TARGETS}")
endif()
