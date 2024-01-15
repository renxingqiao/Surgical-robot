import open3d as o3d
import numpy as np

def view_pcd(path):
    if isinstance(path, str):
        pcd = o3d.io.read_point_cloud(path)
        o3d.visualization.draw_geometries([pcd])
    
    elif isinstance(path, list):
        pass

    else:
        o3d.visualization.draw_geometries([path])

def multy_pcd(path_list):

    # 读取第一个PCD文件
    pcd1 = o3d.io.read_point_cloud(path_list[0])

    # 读取第二个PCD文件
    pcd2 = o3d.io.read_point_cloud(path_list[1])

    # 设置第一个点云的颜色（例如，红色）
    pcd1.paint_uniform_color([1, 0, 0])

    # 设置第二个点云的颜色（例如，绿色）
    pcd2.paint_uniform_color([0, 1, 0])

    # 创建可视化窗口
    vis = o3d.visualization.Visualizer()

    # 添加两个点云到可视化窗口
    vis.create_window()
    vis.add_geometry(pcd1)
    vis.add_geometry(pcd2)

    # 设置视角，以便将两个点云一起显示
    vis.get_view_control().set_lookat([0, 0, 0])  # 设置观察点位置
    vis.get_view_control().set_up([0, 1, 0])     # 设置观察点的上方向

    # 显示点云
    vis.run()
    vis.destroy_window()



def show_japanese_ball():

    # 定义椭球体的参数
    center = [0, 0, 0]  # 椭球体的中心坐标
    radii = [1, 2, 3]   # 椭球体的半径，分别对应x、y、z轴
    num_points = 1000    # 生成的点的数量

    # 生成随机点在单位球内
    points = np.random.randn(num_points, 3)
    norms = np.linalg.norm(points, axis=1)
    points_normalized = points / norms[:, np.newaxis]

    # 将单位球点坐标缩放到椭球体大小
    points_scaled = radii * points_normalized

    # 平移到椭球体中心
    points_final = points_scaled + center

    # 创建点云对象
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points_final)

    # # 保存点云为PCD文件
    o3d.io.write_point_cloud("data/registration/ellipsoid.pcd", point_cloud)

    # 显示点云（可选）
    o3d.visualization.draw_geometries([point_cloud])


def np2pcd(array):
    pcd = o3d.geometry.PointCloud() 
    pcd.points = o3d.utility.Vector3dVector(array) 
    
    return pcd
