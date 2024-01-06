import numpy as np
import open3d as o3d

# 1. Read the original point cloud file
original_point_cloud = o3d.io.read_point_cloud("data/registration/ellipsoid.pcd")

# 2. Generate random translation and rotation transformations
translation = np.random.uniform(-0.1, 0.1, size=(3,))
rotation_axis = np.random.uniform(-1.0, 1.0, size=(3,))
rotation_angle = np.random.uniform(0, 360)


# 3. Apply translation and rotation transformations to the point cloud
transformed_point_cloud = o3d.io.read_point_cloud("data/registration/ellipsoid.pcd")  # Create a copy of the original point cloud
transformed_point_cloud.translate(translation)

# 4. Perform point cloud registration
threshold = 0.00000001  # Registration threshold
trans_init = np.identity(4)  # Initial transformation matrix
reg_p2p = o3d.pipelines.registration.registration_icp(
    transformed_point_cloud, original_point_cloud, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPoint(),
    o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=1000))

# 5. Apply the registration transformation to the point cloud
transformed_point_cloud_registered = transformed_point_cloud.transform(reg_p2p.transformation)

# 6. Calculate the center points of the original and registered point clouds
original_center = np.asarray(original_point_cloud.get_center())
registered_center = np.asarray(transformed_point_cloud_registered.get_center())

# 7. Calculate the center point error
center_error = np.linalg.norm(original_center - registered_center)

print("Original point cloud center coordinates:", original_center)
print("Registered point cloud center coordinates:", registered_center)
print("Center point error:", center_error)
