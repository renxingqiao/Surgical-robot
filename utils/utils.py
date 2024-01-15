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

    # ��ȡ��һ��PCD�ļ�
    pcd1 = o3d.io.read_point_cloud(path_list[0])

    # ��ȡ�ڶ���PCD�ļ�
    pcd2 = o3d.io.read_point_cloud(path_list[1])

    # ���õ�һ�����Ƶ���ɫ�����磬��ɫ��
    pcd1.paint_uniform_color([1, 0, 0])

    # ���õڶ������Ƶ���ɫ�����磬��ɫ��
    pcd2.paint_uniform_color([0, 1, 0])

    # �������ӻ�����
    vis = o3d.visualization.Visualizer()

    # ����������Ƶ����ӻ�����
    vis.create_window()
    vis.add_geometry(pcd1)
    vis.add_geometry(pcd2)

    # �����ӽǣ��Ա㽫��������һ����ʾ
    vis.get_view_control().set_lookat([0, 0, 0])  # ���ù۲��λ��
    vis.get_view_control().set_up([0, 1, 0])     # ���ù۲����Ϸ���

    # ��ʾ����
    vis.run()
    vis.destroy_window()



def show_japanese_ball():

    # ����������Ĳ���
    center = [0, 0, 0]  # ���������������
    radii = [1, 2, 3]   # ������İ뾶���ֱ��Ӧx��y��z��
    num_points = 1000    # ���ɵĵ������

    # ����������ڵ�λ����
    points = np.random.randn(num_points, 3)
    norms = np.linalg.norm(points, axis=1)
    points_normalized = points / norms[:, np.newaxis]

    # ����λ����������ŵ��������С
    points_scaled = radii * points_normalized

    # ƽ�Ƶ�����������
    points_final = points_scaled + center

    # �������ƶ���
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points_final)

    # # �������ΪPCD�ļ�
    o3d.io.write_point_cloud("data/registration/ellipsoid.pcd", point_cloud)

    # ��ʾ���ƣ���ѡ��
    o3d.visualization.draw_geometries([point_cloud])


def np2pcd(array):
    pcd = o3d.geometry.PointCloud() 
    pcd.points = o3d.utility.Vector3dVector(array) 
    
    return pcd
