// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from active_perception_interfaces:msg/HeuristicMetrics.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__struct.h"
#include "active_perception_interfaces/msg/detail/heuristic_metrics__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool active_perception_interfaces__msg__heuristic_metrics__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[69];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("active_perception_interfaces.msg._heuristic_metrics.HeuristicMetrics", full_classname_dest, 68) == 0);
  }
  active_perception_interfaces__msg__HeuristicMetrics * ros_message = _ros_message;
  {  // sharpness_score
    PyObject * field = PyObject_GetAttrString(_pymsg, "sharpness_score");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->sharpness_score = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // illumination_score
    PyObject * field = PyObject_GetAttrString(_pymsg, "illumination_score");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->illumination_score = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // bbox_area_ratio
    PyObject * field = PyObject_GetAttrString(_pymsg, "bbox_area_ratio");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bbox_area_ratio = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * active_perception_interfaces__msg__heuristic_metrics__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HeuristicMetrics */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("active_perception_interfaces.msg._heuristic_metrics");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HeuristicMetrics");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  active_perception_interfaces__msg__HeuristicMetrics * ros_message = (active_perception_interfaces__msg__HeuristicMetrics *)raw_ros_message;
  {  // sharpness_score
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->sharpness_score);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sharpness_score", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // illumination_score
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->illumination_score);
    {
      int rc = PyObject_SetAttrString(_pymessage, "illumination_score", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bbox_area_ratio
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bbox_area_ratio);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bbox_area_ratio", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
