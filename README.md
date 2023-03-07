# Surgical-robot
用于脑卒中的手术机器人

这是一个项目说明文档

## 1 概述

本项目基于Realsense-D455及JAKA机器人进行脑部手术钻孔定位，该任务包括以下几个步骤

1、通过三维重建技术对人脑部CT进行**重建**，得到**携带病变位置信息**的患者头部模型

2、利用深度相机实时获取人脸，利用人脸分割技术获取**面部点云及特征**

3、以面部点云为目标点云，头部点云为源点云，进行**配准**，得到相机坐标系下脑内病变坐标

4、将相机固定至机械臂，进行手眼标定，将相机坐标系下的病变坐标转换为**机械臂坐标系下的坐标**

5、设置上游任务，对机械臂进行路径、轨迹规划，移动至头部开创位置，辅助医生完成手术

## 三维重建

通过CT对患者脑部CT进行重建



通过不同分割算法提取头部主干点云特征（下图效果更佳）

![Screenshot from 2023-03-02 15-30-34](https://user-images.githubusercontent.com/88017321/222361029-95d35dbd-1bb5-450e-a9f0-9fee160c9135.png)

![Screenshot from 2023-03-02 15-31-01](https://user-images.githubusercontent.com/88017321/222360896-8b896e54-2289-46d0-bca4-30f9d93ddb1d.png)

## 人脸分割（两种范式）

基于dilib库、opencv及深度图进行人脸分割

![Screenshot from 2023-03-02 15-37-59](https://user-images.githubusercontent.com/88017321/222362277-acb99bfb-59d4-4e47-9ac6-a0ace9bfb24c.png)

![Screenshot from 2023-03-02 15-37-59](https://user-images.githubusercontent.com/88017321/222362352-62e57fa0-2906-4290-b019-c131dc7d22ce.png)

![Screenshot from 2023-03-02 15-38-48](https://user-images.githubusercontent.com/88017321/222362439-0eaac645-6534-42b3-a22d-6a7d1c7ea6f1.png)

基于深度学习的点云分割

![Screenshot from 2023-03-02 15-46-02](https://user-images.githubusercontent.com/88017321/222364068-009e4222-9e5d-44f7-9e5d-4a890a19b56f.png)

## 面部点云配准

RANSAC及NDT并未达到良好的效果

我们使用的配准算法

![Screenshot from 2022-09-14 18-40-13](https://user-images.githubusercontent.com/88017321/222365875-a17e86d0-94a4-4821-82ca-ac9562e096fc.png)

![Screenshot from 2022-09-14 19-11-27](https://user-images.githubusercontent.com/88017321/222365913-0963cc54-c8e8-4092-904c-d1a0f519e1d9.png)

TODO：基于深度学习的配准算法

## 手眼标定

基于ROS系统及ARUCO码进行位姿解算，用于得到变换矩阵，解算病变相对于机械臂的位姿。

## 机械臂控制

通过求逆解得到机械臂各个关节最终目标值，基于目标值进行路径规划和轨迹规划，最终令机械臂到达手术空间。




