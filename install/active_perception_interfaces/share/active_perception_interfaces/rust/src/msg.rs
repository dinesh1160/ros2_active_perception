#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to active_perception_interfaces__msg__HeuristicMetrics

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::HeuristicMetrics::default())
  }
}

impl rosidl_runtime_rs::Message for HeuristicMetrics {
  type RmwMsg = super::msg::rmw::HeuristicMetrics;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sharpness_score: msg.sharpness_score,
        illumination_score: msg.illumination_score,
        bbox_area_ratio: msg.bbox_area_ratio,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      sharpness_score: msg.sharpness_score,
      illumination_score: msg.illumination_score,
      bbox_area_ratio: msg.bbox_area_ratio,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      sharpness_score: msg.sharpness_score,
      illumination_score: msg.illumination_score,
      bbox_area_ratio: msg.bbox_area_ratio,
    }
  }
}


