"""
transform
"""
import numpy as np
from scipy.spatial.transform import Rotation as R

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, Pose, Quaternion, Point, PointStamped, Transform, TransformStamped


def transform_to_tr(tf: Transform) -> tuple[np.ndarray, np.ndarray]:
    """
    return translation(3,), rotation(3,3)
    """
    t = np.array([tf.translation.x, tf.translation.y, tf.translation.z])
    q = np.array([tf.rotation.x, tf.rotation.y,
                  tf.rotation.z, tf.rotation.w])
    # scale-last quaterion: xyzw
    rotation = R.from_quat(q)
    r = rotation.as_matrix()

    return t,r


def transformstamped_to_tr(tfstamped: TransformStamped) -> tuple[np.ndarray, np.ndarray]:
    """
    return translation(3,), rotation(3,3)
    """
    return transform_to_tr(tfstamped.transform)