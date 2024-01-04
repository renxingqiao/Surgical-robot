# -*- coding: utf-8 -*-
import pybullet as p
import math

# ��ʼ��PyBullet��������
p.connect(p.GUI)  # ʹ�ÿ��ӻ�ģʽ����

# ����������
rectangle_id = p.createCollisionShape(p.GEOM_BOX, halfExtents=[1, 1, 2])
rectangle_body_id = p.createMultiBody(baseCollisionShapeIndex=rectangle_id, basePosition=[0, 0, 0])

# ����Բ����
cylinder_id = p.createCollisionShape(p.GEOM_CYLINDER, radius=1, height=4)
cylinder_body_id = p.createMultiBody(baseCollisionShapeIndex=cylinder_id, basePosition=[1, 1, 2])

# ���ó��������ת����Z����ת45�ȣ�
angle = math.radians(45)  # ���Ƕ�ת��Ϊ����
rotation_matrix = p.getMatrixFromQuaternion(p.getQuaternionFromEuler([0, 0, angle]))
p.resetBasePositionAndOrientation(rectangle_body_id, [0, 0, 0], [0, 0, 0, 1])

# ����Բ�������ת����X����ת30�ȣ�
angle = math.radians(30)  # ���Ƕ�ת��Ϊ����
rotation_matrix = p.getMatrixFromQuaternion(p.getQuaternionFromEuler([angle, 0, 0]))
p.resetBasePositionAndOrientation(cylinder_body_id, [1, 1, 5], [0, 1, 0, 1])

# �����ɺ�ɫ�ĺ���
def turn_objects_red():
    p.changeVisualShape(rectangle_body_id, -1, rgbaColor=[1, 0, 0, 1])  # ���������ɺ�ɫ
    p.changeVisualShape(cylinder_body_id, -1, rgbaColor=[1, 0, 0, 1])   # ��Բ�����ɺ�ɫ

# ������ײ���
contacts = p.getContactPoints(bodyA=rectangle_body_id, bodyB=cylinder_body_id)

if contacts:
    print("The cylinder and rectangle are colliding.")
    turn_objects_red()  # �����ײ�������������ɺ�ɫ
else:
    print("The cylinder and rectangle are not colliding.")

# ������С����
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
# �ر�PyBullet��������
# p.disconnect()