// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from active_perception_interfaces:srv/AnalyzeQuality.idl
// generated code does not contain a copyright notice
#include "active_perception_interfaces/srv/detail/analyze_quality__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `image`
#include "sensor_msgs/msg/detail/image__functions.h"

bool
active_perception_interfaces__srv__AnalyzeQuality_Request__init(active_perception_interfaces__srv__AnalyzeQuality_Request * msg)
{
  if (!msg) {
    return false;
  }
  // image
  if (!sensor_msgs__msg__Image__init(&msg->image)) {
    active_perception_interfaces__srv__AnalyzeQuality_Request__fini(msg);
    return false;
  }
  return true;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Request__fini(active_perception_interfaces__srv__AnalyzeQuality_Request * msg)
{
  if (!msg) {
    return;
  }
  // image
  sensor_msgs__msg__Image__fini(&msg->image);
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Request__are_equal(const active_perception_interfaces__srv__AnalyzeQuality_Request * lhs, const active_perception_interfaces__srv__AnalyzeQuality_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // image
  if (!sensor_msgs__msg__Image__are_equal(
      &(lhs->image), &(rhs->image)))
  {
    return false;
  }
  return true;
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Request__copy(
  const active_perception_interfaces__srv__AnalyzeQuality_Request * input,
  active_perception_interfaces__srv__AnalyzeQuality_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // image
  if (!sensor_msgs__msg__Image__copy(
      &(input->image), &(output->image)))
  {
    return false;
  }
  return true;
}

active_perception_interfaces__srv__AnalyzeQuality_Request *
active_perception_interfaces__srv__AnalyzeQuality_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Request * msg = (active_perception_interfaces__srv__AnalyzeQuality_Request *)allocator.allocate(sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request));
  bool success = active_perception_interfaces__srv__AnalyzeQuality_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Request__destroy(active_perception_interfaces__srv__AnalyzeQuality_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    active_perception_interfaces__srv__AnalyzeQuality_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__init(active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Request * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request)) {
      return false;
    }
    data = (active_perception_interfaces__srv__AnalyzeQuality_Request *)allocator.zero_allocate(size, sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = active_perception_interfaces__srv__AnalyzeQuality_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        active_perception_interfaces__srv__AnalyzeQuality_Request__fini(&data[i - 1]);
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
active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__fini(active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * array)
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
      active_perception_interfaces__srv__AnalyzeQuality_Request__fini(&array->data[i]);
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

active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence *
active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * array = (active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence *)allocator.allocate(sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__destroy(active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__are_equal(const active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * lhs, const active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!active_perception_interfaces__srv__AnalyzeQuality_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__copy(
  const active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * input,
  active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(active_perception_interfaces__srv__AnalyzeQuality_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    active_perception_interfaces__srv__AnalyzeQuality_Request * data =
      (active_perception_interfaces__srv__AnalyzeQuality_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!active_perception_interfaces__srv__AnalyzeQuality_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          active_perception_interfaces__srv__AnalyzeQuality_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!active_perception_interfaces__srv__AnalyzeQuality_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `reasoning`
#include "rosidl_runtime_c/string_functions.h"

bool
active_perception_interfaces__srv__AnalyzeQuality_Response__init(active_perception_interfaces__srv__AnalyzeQuality_Response * msg)
{
  if (!msg) {
    return false;
  }
  // occlusion_score
  // framing_score
  // reasoning
  if (!rosidl_runtime_c__String__init(&msg->reasoning)) {
    active_perception_interfaces__srv__AnalyzeQuality_Response__fini(msg);
    return false;
  }
  return true;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Response__fini(active_perception_interfaces__srv__AnalyzeQuality_Response * msg)
{
  if (!msg) {
    return;
  }
  // occlusion_score
  // framing_score
  // reasoning
  rosidl_runtime_c__String__fini(&msg->reasoning);
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Response__are_equal(const active_perception_interfaces__srv__AnalyzeQuality_Response * lhs, const active_perception_interfaces__srv__AnalyzeQuality_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // occlusion_score
  if (lhs->occlusion_score != rhs->occlusion_score) {
    return false;
  }
  // framing_score
  if (lhs->framing_score != rhs->framing_score) {
    return false;
  }
  // reasoning
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->reasoning), &(rhs->reasoning)))
  {
    return false;
  }
  return true;
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Response__copy(
  const active_perception_interfaces__srv__AnalyzeQuality_Response * input,
  active_perception_interfaces__srv__AnalyzeQuality_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // occlusion_score
  output->occlusion_score = input->occlusion_score;
  // framing_score
  output->framing_score = input->framing_score;
  // reasoning
  if (!rosidl_runtime_c__String__copy(
      &(input->reasoning), &(output->reasoning)))
  {
    return false;
  }
  return true;
}

active_perception_interfaces__srv__AnalyzeQuality_Response *
active_perception_interfaces__srv__AnalyzeQuality_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Response * msg = (active_perception_interfaces__srv__AnalyzeQuality_Response *)allocator.allocate(sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response));
  bool success = active_perception_interfaces__srv__AnalyzeQuality_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Response__destroy(active_perception_interfaces__srv__AnalyzeQuality_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    active_perception_interfaces__srv__AnalyzeQuality_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__init(active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Response * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response)) {
      return false;
    }
    data = (active_perception_interfaces__srv__AnalyzeQuality_Response *)allocator.zero_allocate(size, sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = active_perception_interfaces__srv__AnalyzeQuality_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        active_perception_interfaces__srv__AnalyzeQuality_Response__fini(&data[i - 1]);
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
active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__fini(active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * array)
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
      active_perception_interfaces__srv__AnalyzeQuality_Response__fini(&array->data[i]);
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

active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence *
active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * array = (active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence *)allocator.allocate(sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__destroy(active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__are_equal(const active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * lhs, const active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!active_perception_interfaces__srv__AnalyzeQuality_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__copy(
  const active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * input,
  active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(active_perception_interfaces__srv__AnalyzeQuality_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    active_perception_interfaces__srv__AnalyzeQuality_Response * data =
      (active_perception_interfaces__srv__AnalyzeQuality_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!active_perception_interfaces__srv__AnalyzeQuality_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          active_perception_interfaces__srv__AnalyzeQuality_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!active_perception_interfaces__srv__AnalyzeQuality_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "active_perception_interfaces/srv/detail/analyze_quality__functions.h"

bool
active_perception_interfaces__srv__AnalyzeQuality_Event__init(active_perception_interfaces__srv__AnalyzeQuality_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    active_perception_interfaces__srv__AnalyzeQuality_Event__fini(msg);
    return false;
  }
  // request
  if (!active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__init(&msg->request, 0)) {
    active_perception_interfaces__srv__AnalyzeQuality_Event__fini(msg);
    return false;
  }
  // response
  if (!active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__init(&msg->response, 0)) {
    active_perception_interfaces__srv__AnalyzeQuality_Event__fini(msg);
    return false;
  }
  return true;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Event__fini(active_perception_interfaces__srv__AnalyzeQuality_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__fini(&msg->request);
  // response
  active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__fini(&msg->response);
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Event__are_equal(const active_perception_interfaces__srv__AnalyzeQuality_Event * lhs, const active_perception_interfaces__srv__AnalyzeQuality_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Event__copy(
  const active_perception_interfaces__srv__AnalyzeQuality_Event * input,
  active_perception_interfaces__srv__AnalyzeQuality_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

active_perception_interfaces__srv__AnalyzeQuality_Event *
active_perception_interfaces__srv__AnalyzeQuality_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Event * msg = (active_perception_interfaces__srv__AnalyzeQuality_Event *)allocator.allocate(sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event));
  bool success = active_perception_interfaces__srv__AnalyzeQuality_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Event__destroy(active_perception_interfaces__srv__AnalyzeQuality_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    active_perception_interfaces__srv__AnalyzeQuality_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__init(active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Event * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event)) {
      return false;
    }
    data = (active_perception_interfaces__srv__AnalyzeQuality_Event *)allocator.zero_allocate(size, sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = active_perception_interfaces__srv__AnalyzeQuality_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        active_perception_interfaces__srv__AnalyzeQuality_Event__fini(&data[i - 1]);
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
active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__fini(active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * array)
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
      active_perception_interfaces__srv__AnalyzeQuality_Event__fini(&array->data[i]);
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

active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence *
active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * array = (active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence *)allocator.allocate(sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__destroy(active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__are_equal(const active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * lhs, const active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!active_perception_interfaces__srv__AnalyzeQuality_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence__copy(
  const active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * input,
  active_perception_interfaces__srv__AnalyzeQuality_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(active_perception_interfaces__srv__AnalyzeQuality_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    active_perception_interfaces__srv__AnalyzeQuality_Event * data =
      (active_perception_interfaces__srv__AnalyzeQuality_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!active_perception_interfaces__srv__AnalyzeQuality_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          active_perception_interfaces__srv__AnalyzeQuality_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!active_perception_interfaces__srv__AnalyzeQuality_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
