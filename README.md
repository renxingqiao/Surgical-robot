# Surgical-robot
用于脑卒中的手术机器人

这是一个项目说明文档

## 1 概述

本项目基于Realsense-D455及JAKA机器人进行脑部手术钻孔定位，该任务包括以下几个步骤

1、通过三维重建技术对人脑部CT进行**重建**，得到**携带病变位置信息**的患者头部模型

2、利用深度相机实时获取人脸**面部点云及特征**

3、以面部点云为目标点云，头部点云为源点云，进行**配准**，得到相机坐标系下脑内病变坐标

4、将相机固定至机械臂，进行手眼标定，将相机坐标系下的病变坐标转换为**机械臂坐标系下的坐标**

5、设置上游任务，对机械臂进行路径、轨迹规划，移动至头部开创位置，辅助医生完成手术

