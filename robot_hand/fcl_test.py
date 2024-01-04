# -*- coding: utf-8 -*-
import fcl
import numpy as np


box = fcl.Box(1, 1, 1)          
sphere = fcl.Sphere(1)          


T = np.array([1.0, 2.0, 3.0])
q = np.array([0.707, 0.0, 0.0, 0.707]) 
box_tf = fcl.Transform(q, T)
sphere_tf = fcl.Transform(q, T)  

box_obj = fcl.CollisionObject(box,box_tf) 
sphere_obj = fcl.CollisionObject(sphere,sphere_tf)


request = fcl.CollisionRequest()
result = fcl.CollisionResult()
ret = fcl.collide(box_obj, sphere_obj, request, result)
print("result 1",result.is_collision)


request = fcl.DistanceRequest()
result = fcl.DistanceResult()
ret = fcl.distance(box_obj, sphere_obj, request, result)
print("result 2",result.min_distance)

request = fcl.ContinuousCollisionRequest()
result = fcl.ContinuousCollisionResult()
ret = fcl.continuousCollide(sphere_obj, sphere_tf, box_obj, box_tf, request, result)
print("result 3",result.is_collide)

