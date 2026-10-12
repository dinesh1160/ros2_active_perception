# Header is copied from the snapshot image so the coordinator can match results
std_msgs/Header header
# False when YOLO found no target in the snapshot (scores are then zero)
bool target_detected
float32 sharpness_score
float32 illumination_score
float32 bbox_area_ratio
