# Header is copied from the snapshot image so the coordinator can match results
std_msgs/Header header
# False when YOLO found no target in the snapshot (scores are then zero)
bool target_detected
float32 sharpness_score
float32 illumination_score
float32 bbox_area_ratio
# Target bounding box in pixels (clamped to the image)
float32 bbox_x_min
float32 bbox_y_min
float32 bbox_x_max
float32 bbox_y_max
