import utils.utils as u
import open3d as o3d
import numpy as np

if __name__ == '__main__':
    # path = ['/home/fan/PCL_project/k4pcs/result/icp_result.pcd', "/home/fan/PCL_project/k4pcs/result/pcs.pcd"]
    # u.multy_pcd(path)
    path = "/home/fan/Downloads/pc.ply"
    pcd = o3d.io.read_point_cloud(path)
    points = np.asarray(pcd.points)

    # half_points = points[:(points.shape[0] / 2), :]
    # import pdb;pdb.set_trace()
    u.view_pcd(pcd)
    
    half_points = points[:1152000, :]
    half_pcd = u.np2pcd(half_points)
    u.view_pcd(half_pcd)

    half_points = points[1152000:, :]
    half_pcd = u.np2pcd(half_points)

    
    u.view_pcd(half_pcd)

    # print(points.shape)
    # u.show_japanese_ball()