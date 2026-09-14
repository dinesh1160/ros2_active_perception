// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice
#include "active_perception_interfaces/msg/detail/heuristic_metrics__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
active_perception_interfaces__msg__HeuristicMetrics__init(active_perception_interfaces__msg__HeuristicMetrics * msg)
{
  if (!msg) {
    return false;
  }
  // sharpness_score
  // illumination_score
  // bbox_area_ratio
  return true;
}

void
active_perception_interfaces__msg__HeuristicMetrics__fini(active_perception_interfaces__msg__HeuristicMetrics * msg)
{
  if (!msg) {
    return;
  }
  // sharpness_score
  // illumination_score
  // bbox_area_ratio
}

bool
active_perception_interfaces__msg__HeuristicMetrics__are_equal(const active_perception_interfaces__msg__HeuristicMetrics * lhs, const active_perception_interfaces__msg__HeuristicMetrics * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sharpness_score
  if (lhs->sharpness_score != rhs->sharpness_score) {
    return false;
  }
  // illumination_score
  if (lhs->illumination_score != rhs->illumination_score) {
    return false;
  }
  // bbox_area_ratio
  if (lhs->bbox_area_ratio != rhs->bbox_area_ratio) {
    return false;
  }
  return true;
}

bool
active_perception_interfaces__msg__HeuristicMetrics__copy(
  const active_perception_interfaces__msg__HeuristicMetrics * input,
  active_perception_interfaces__msg__HeuristicMetrics * output)
{
  if (!input || !output) {
    return false;
  }
  // sharpness_score
  output->sharpness_score = input->sharpness_score;
  // illumination_score
  output->illumination_score = input->illumination_score;
  // bbox_area_ratio
  output->bbox_area_ratio = input->bbox_area_ratio;
  return true;
}

active_perception_interfaces__msg__HeuristicMetrics *
active_perception_interfaces__msg__HeuristicMetrics__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__msg__HeuristicMetrics * msg = (active_perception_interfaces__msg__HeuristicMetrics *)allocator.allocate(sizeof(active_perception_interfaces__msg__HeuristicMetrics), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(active_perception_interfaces__msg__HeuristicMetrics));
  bool success = active_perception_interfaces__msg__HeuristicMetrics__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
active_perception_interfaces__msg__HeuristicMetrics__destroy(active_perception_interfaces__msg__HeuristicMetrics * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    active_perception_interfaces__msg__HeuristicMetrics__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
active_perception_interfaces__msg__HeuristicMetrics__Sequence__init(active_perception_interfaces__msg__HeuristicMetrics__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__msg__HeuristicMetrics * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(active_perception_interfaces__msg__HeuristicMetrics)) {
      return false;
    }
    data = (active_perception_interfaces__msg__HeuristicMetrics *)allocator.zero_allocate(size, sizeof(active_perception_interfaces__msg__HeuristicMetrics), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = active_perception_interfaces__msg__HeuristicMetrics__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        active_perception_interfaces__msg__HeuristicMetrics__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
active_perception_interfaces__msg__HeuristicMetrics__Sequence__fini(active_perception_interfaces__msg__HeuristicMetrics__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      active_perception_interfaces__msg__HeuristicMetrics__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

active_perception_interfaces__msg__HeuristicMetrics__Sequence *
active_perception_interfaces__msg__HeuristicMetrics__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__msg__HeuristicMetrics__Sequence * array = (active_perception_interfaces__msg__HeuristicMetrics__Sequence *)allocator.allocate(sizeof(active_perception_interfaces__msg__HeuristicMetrics__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = active_perception_interfaces__msg__HeuristicMetrics__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
active_perception_interfaces__msg__HeuristicMetrics__Sequence__destroy(active_perception_interfaces__msg__HeuristicMetrics__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    active_perception_interfaces__msg__HeuristicMetrics__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
active_perception_interfaces__msg__HeuristicMetrics__Sequence__are_equal(const active_perception_interfaces__msg__HeuristicMetrics__Sequence * lhs, const active_perception_interfaces__msg__HeuristicMetrics__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!active_perception_interfaces__msg__HeuristicMetrics__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
active_perception_interfaces__msg__HeuristicMetrics__Sequence__copy(
  const active_perception_interfaces__msg__HeuristicMetrics__Sequence * input,
  active_perception_interfaces__msg__HeuristicMetrics__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(active_perception_interfaces__msg__HeuristicMetrics)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(active_perception_interfaces__msg__HeuristicMetrics);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    active_perception_interfaces__msg__HeuristicMetrics * data =
      (active_perception_interfaces__msg__HeuristicMetrics *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!active_perception_interfaces__msg__HeuristicMetrics__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          active_perception_interfaces__msg__HeuristicMetrics__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!active_perception_interfaces__msg__HeuristicMetrics__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
