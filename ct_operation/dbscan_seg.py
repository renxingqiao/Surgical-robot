# -*- encoding:utf-8 -*-
import open3d as o3d
from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import time

def load_ply(file_path):
    pcd = o3d.io.read_point_cloud(file_path)
    return pcd

def extract_point_cloud(pcd):
    points = np.asarray(pcd.points)
    return points

def perform_dbscan(points, eps, min_samples):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    start = time.time()
    labels = dbscan.fit_predict(points)
    end = time.time()
    print(f"time costing {(end - start)} ")
    return labels


def visualize_clusters(points, labels):
    unique_labels = np.unique(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

    # main_index = np.where(labels == -1)[0]
    # main_points = points[main_index]
    for i in range(-1, max(labels)):
        indexs = np.where(labels == i)[0]
        if (indexs.shape[0] < 700): continue
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points[indexs])
        o3d.visualization.draw_geometries([pcd], window_name="DBSCAN Clusters")

        
    

    
    # pcd.points = o3d.utility.Vector3dVector(main_points)
    # for label, color in zip(unique_labels, colors):
    #     if label == -1:
            
    #         noise_mask = (labels == label)
    #         pcd_noise = o3d.geometry.PointCloud()
    #         pcd_noise.points = o3d.utility.Vector3dVector(points[noise_mask])
    #         pcd_noise.paint_uniform_color([0, 0, 0])  
    #         pcd += pcd_noise
    #     else:
    #         cluster_mask = (labels == label)
    #         pcd_cluster = o3d.geometry.PointCloud()
    #         pcd_cluster.points = o3d.utility.Vector3dVector(points[cluster_mask])
    #         color_rgb = color[:-1]  
    #         pcd_cluster.paint_uniform_color(color_rgb)
    #         pcd += pcd_cluster

    # o3d.visualization.draw_geometries([pcd], window_name="DBSCAN Clusters")

if __name__ == "__main__":
    
    ply_file_path = '/home/fan/Surgical-robot/ct_operation/data/Mesh_barrier.ply'

    
    point_cloud = load_ply(ply_file_path)

    
    points = extract_point_cloud(point_cloud)

    
    eps = 1  
    min_samples = 10

    
    labels = perform_dbscan(points, eps, min_samples)

    
    visualize_clusters(points, labels)
