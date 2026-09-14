#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "active_perception_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__active_perception_interfaces__msg__HeuristicMetrics() -> *const std::ffi::c_void;
}

#[link(name = "active_perception_interfaces__rosidl_generator_c")]
extern "C" {
    fn active_perception_interfaces__msg__HeuristicMetrics__init(msg: *mut HeuristicMetrics) -> bool;
    fn active_perception_interfaces__msg__HeuristicMetrics__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<HeuristicMetrics>, size: usize) -> bool;
    fn active_perception_interfaces__msg__HeuristicMetrics__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<HeuristicMetrics>);
    fn active_perception_interfaces__msg__HeuristicMetrics__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<HeuristicMetrics>, out_seq: *mut rosidl_runtime_rs::Sequence<HeuristicMetrics>) -> bool;
}

// Corresponds to active_perception_interfaces__msg__HeuristicMetrics
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct HeuristicMetrics {

    // This member is not documented.
    #[allow(missing_docs)]
    pub sharpness_score: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub illumination_score: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub bbox_area_ratio: f32,

}



impl Default for HeuristicMetrics {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !active_perception_interfaces__msg__HeuristicMetrics__init(&mut msg as *mut _) {
        panic!("Call to active_perception_interfaces__msg__HeuristicMetrics__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for HeuristicMetrics {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__msg__HeuristicMetrics__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__msg__HeuristicMetrics__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__msg__HeuristicMetrics__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for HeuristicMetrics {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for HeuristicMetrics where Self: Sized {
  const TYPE_NAME: &'static str = "active_perception_interfaces/msg/HeuristicMetrics";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__active_perception_interfaces__msg__HeuristicMetrics() }
  }
}


