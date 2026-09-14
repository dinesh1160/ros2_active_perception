#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to active_perception_interfaces__srv__AnalyzeQuality_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AnalyzeQuality_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub image: sensor_msgs::msg::Image,

}



impl Default for AnalyzeQuality_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AnalyzeQuality_Request::default())
  }
}

impl rosidl_runtime_rs::Message for AnalyzeQuality_Request {
  type RmwMsg = super::srv::rmw::AnalyzeQuality_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        image: sensor_msgs::msg::Image::into_rmw_message(std::borrow::Cow::Owned(msg.image)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        image: sensor_msgs::msg::Image::into_rmw_message(std::borrow::Cow::Borrowed(&msg.image)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      image: sensor_msgs::msg::Image::from_rmw_message(msg.image),
    }
  }
}


// Corresponds to active_perception_interfaces__srv__AnalyzeQuality_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    pub reasoning: std::string::String,

}



impl Default for AnalyzeQuality_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AnalyzeQuality_Response::default())
  }
}

impl rosidl_runtime_rs::Message for AnalyzeQuality_Response {
  type RmwMsg = super::srv::rmw::AnalyzeQuality_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        occlusion_score: msg.occlusion_score,
        framing_score: msg.framing_score,
        reasoning: msg.reasoning.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      occlusion_score: msg.occlusion_score,
      framing_score: msg.framing_score,
        reasoning: msg.reasoning.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      occlusion_score: msg.occlusion_score,
      framing_score: msg.framing_score,
      reasoning: msg.reasoning.to_string(),
    }
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


