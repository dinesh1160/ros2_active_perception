#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "active_perception_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__active_perception_interfaces__srv__AnalyzeQuality_Request() -> *const std::ffi::c_void;
}

#[link(name = "active_perception_interfaces__rosidl_generator_c")]
extern "C" {
    fn active_perception_interfaces__srv__AnalyzeQuality_Request__init(msg: *mut AnalyzeQuality_Request) -> bool;
    fn active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AnalyzeQuality_Request>, size: usize) -> bool;
    fn active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AnalyzeQuality_Request>);
    fn active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AnalyzeQuality_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<AnalyzeQuality_Request>) -> bool;
}

// Corresponds to active_perception_interfaces__srv__AnalyzeQuality_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AnalyzeQuality_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub image: sensor_msgs::msg::rmw::Image,

}



impl Default for AnalyzeQuality_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !active_perception_interfaces__srv__AnalyzeQuality_Request__init(&mut msg as *mut _) {
        panic!("Call to active_perception_interfaces__srv__AnalyzeQuality_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AnalyzeQuality_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__srv__AnalyzeQuality_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AnalyzeQuality_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AnalyzeQuality_Request where Self: Sized {
  const TYPE_NAME: &'static str = "active_perception_interfaces/srv/AnalyzeQuality_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__active_perception_interfaces__srv__AnalyzeQuality_Request() }
  }
}


#[link(name = "active_perception_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__active_perception_interfaces__srv__AnalyzeQuality_Response() -> *const std::ffi::c_void;
}

#[link(name = "active_perception_interfaces__rosidl_generator_c")]
extern "C" {
    fn active_perception_interfaces__srv__AnalyzeQuality_Response__init(msg: *mut AnalyzeQuality_Response) -> bool;
    fn active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AnalyzeQuality_Response>, size: usize) -> bool;
    fn active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AnalyzeQuality_Response>);
    fn active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AnalyzeQuality_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<AnalyzeQuality_Response>) -> bool;
}

// Corresponds to active_perception_interfaces__srv__AnalyzeQuality_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AnalyzeQuality_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub occlusion_score: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub framing_score: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub reasoning: rosidl_runtime_rs::String,

}



impl Default for AnalyzeQuality_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !active_perception_interfaces__srv__AnalyzeQuality_Response__init(&mut msg as *mut _) {
        panic!("Call to active_perception_interfaces__srv__AnalyzeQuality_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AnalyzeQuality_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { active_perception_interfaces__srv__AnalyzeQuality_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AnalyzeQuality_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AnalyzeQuality_Response where Self: Sized {
  const TYPE_NAME: &'static str = "active_perception_interfaces/srv/AnalyzeQuality_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__active_perception_interfaces__srv__AnalyzeQuality_Response() }
  }
}






#[link(name = "active_perception_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__active_perception_interfaces__srv__AnalyzeQuality() -> *const std::ffi::c_void;
}

// Corresponds to active_perception_interfaces__srv__AnalyzeQuality
#[allow(missing_docs, non_camel_case_types)]
pub struct AnalyzeQuality;

impl rosidl_runtime_rs::Service for AnalyzeQuality {
    type Request = AnalyzeQuality_Request;
    type Response = AnalyzeQuality_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__active_perception_interfaces__srv__AnalyzeQuality() }
    }
}


