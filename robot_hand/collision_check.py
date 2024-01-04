# -*- coding: utf-8 -*-
import pybullet as p
import math

# 初始化PyBullet物理引擎
p.connect(p.GUI)  # 使用可视化模式启动

# 创建长方体
rectangle_id = p.createCollisionShape(p.GEOM_BOX, halfExtents=[1, 1, 2])
rectangle_body_id = p.createMultiBody(baseCollisionShapeIndex=rectangle_id, basePosition=[0, 0, 0])

# 创建圆柱体
cylinder_id = p.createCollisionShape(p.GEOM_CYLINDER, radius=1, height=4)
cylinder_body_id = p.createMultiBody(baseCollisionShapeIndex=cylinder_id, basePosition=[1, 1, 2])

# 设置长方体的旋转（绕Z轴旋转45度）
angle = math.radians(45)  # 将角度转换为弧度
rotation_matrix = p.getMatrixFromQuaternion(p.getQuaternionFromEuler([0, 0, angle]))
p.resetBasePositionAndOrientation(rectangle_body_id, [0, 0, 0], [0, 0, 0, 1])

# 设置圆柱体的旋转（绕X轴旋转30度）
angle = math.radians(30)  # 将角度转换为弧度
rotation_matrix = p.getMatrixFromQuaternion(p.getQuaternionFromEuler([angle, 0, 0]))
p.resetBasePositionAndOrientation(cylinder_body_id, [1, 1, 5], [0, 1, 0, 1])

# 定义变成红色的函数
def turn_objects_red():
    p.changeVisualShape(rectangle_body_id, -1, rgbaColor=[1, 0, 0, 1])  # 将长方体变成红色
    p.changeVisualShape(cylinder_body_id, -1, rgbaColor=[1, 0, 0, 1])   # 将圆柱体变成红色

# 进行碰撞检测
contacts = p.getContactPoints(bodyA=rectangle_body_id, bodyB=cylinder_body_id)

if contacts:
    print("The cylinder and rectangle are colliding.")
    turn_objects_red()  # 如果碰撞，将两个物体变成红色
else:
    print("The cylinder and rectangle are not colliding.")

# 计算最小距离
cylinder_pos, _ = p.getBasePositionAndOrientation(cylinder_body_id)
rectangle_pos, _ = p.getBasePositionAndOrientation(rectangle_body_id)

min_distance = p.getClosestPoints(bodyA=cylinder_body_id, bodyB=rectangle_body_id, distance=0.001)
print("*" * 100)
print(min_distance)


if min_distance:
    print("*" * 100)
    print("The minimum distance between the cylinder and rectangle is:", min_distance[0][8])
    print("*" * 100)
else:
    print("No distance information available.")
input()
# 关闭PyBullet物理引擎
# p.disconnect()