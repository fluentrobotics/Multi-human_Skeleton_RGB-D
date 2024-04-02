"""
Convert human keypoint and mask array into skeleton_interfaces message  
"""
import numpy as np

# Message type
from std_msgs.msg import Int32MultiArray, Float32MultiArray, Header, ColorRGBA, MultiArrayDimension
from geometry_msgs.msg import PoseArray, Pose, Quaternion, Point, Point32, PointStamped
from visualization_msgs.msg import Marker, MarkerArray
from sensor_msgs.msg import Image, CompressedImage, CameraInfo
from skeleton_interfaces.msg import MultiHumanSkeleton, HumanSkeleton
from cv_bridge import CvBridge

def keypoints_to_skeleton_interfaces(
        human_id: np.ndarray,
        keypoints_center: np.ndarray,
        keypoints_3d: np.ndarray,
        keypoints_mask: np.ndarray,
        ) -> MultiHumanSkeleton:
    """
    @ human_id: [H,]
    @ keypoints_center: [H,3]
    @ keypoints_3d: [H,K,3]
    @ keypoints_mask: [H,K]

    return skeleton_interfaces.msg.MultiHumanSkeleton
    """
    
    MultiHumanSkeleton_msg = MultiHumanSkeleton()
    MultiHumanSkeleton_msg.multi_human_skeleton = list()

    for idx, id in enumerate(human_id, start=0):
        human_center_array = keypoints_center[idx,...]      # [3,]
        keypoint_data_array = keypoints_3d[idx,...]         # [K,3]
        keypoint_mask_array = keypoints_mask[idx,...]       # [K,]

        human_center = np_vector_to_point32(human_center_array)

        keypoint_data = list()
        for keypoint_vector in keypoint_data_array:
            keypoint_data.append( np_vector_to_point32(keypoint_vector) )

        keypoint_mask = keypoint_mask_array.tolist()

        HumanSkeleton_msg = HumanSkeleton()
        HumanSkeleton_msg.human_id = id.item()
        HumanSkeleton_msg.human_center = human_center
        HumanSkeleton_msg.keypoint_data = keypoint_data
        HumanSkeleton_msg.keypoint_mask = keypoint_mask

        MultiHumanSkeleton_msg.multi_human_skeleton.append(HumanSkeleton_msg)

    return MultiHumanSkeleton_msg

# def dict_to_skeleton_interfaces(human_dict: dict):

def np_vector_to_point32(vector: np.ndarray) -> Point32:
    
    assert vector.shape == (3,), "the shape of vector must be (3,)"
    point = Point32()
    vector_list = vector.tolist()
    point.x = float(vector_list[0])
    point.y = float(vector_list[1])
    point.z = float(vector_list[2])

    return point


def point32_to_np_vector(point: Point32) -> np.ndarray:
    
    point_list = [point.x, point.y, point.z]
    vector = np.array(point_list, dtype=float)
    assert vector.shape == (3,), "the shape of vector must be (3,)"

    return vector