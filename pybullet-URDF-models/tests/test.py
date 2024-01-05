import os
import time
import pybullet as p
import pybullet_data
from urdf_models import models_data
import random

# initialize the GUI and others
jaka_urdf_path = "/home/fan/surgical_test/pybullet-URDF-models/urdf_models/models/jaka/jaka_zu7/jaka_zu7.urdf"
p.connect(p.GUI)
p.resetDebugVisualizerCamera(3, 90, -30, [0.0, -0.0, -0.0])
p.setTimeStep(1 / 240.)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# load urdf data
models = models_data.model_lib()

# load model list
namelist = models.model_name_list
print("Look at what we have {}".format(namelist))

# Load table and plane
p.loadURDF("plane.urdf")
p.loadURDF("table/table.urdf")

# load the randomly picked model
# flags = p.URDF_USE_INERTIA_FROM_FILE
# randomly get a model
# import pdb;pdb.set_trace()
# for i in range(8):
#     random_model = namelist[random.randint(0, len(namelist))] 
#     p.loadURDF(models[random_model], [0., 0., 0.8 + 0.15*i], flags=flags)
jaka_id = p.loadURDF(jaka_urdf_path, [0., 0., 0.8 + 0.15])

# create rect
rectangle_id = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.1, 0.1, 0.1])
rectangle_body_id = p.createMultiBody(baseCollisionShapeIndex=rectangle_id, basePosition=[0, -0.2, 1])
# p.setGravity(0, 0, -9.8)

while 1:
    p.stepSimulation()
    time.sleep(1./240)

    # Get the closest contact points between the robot arm and the rectangle
    contact_points = p.getClosestPoints(jaka_id, rectangle_body_id, 0.01)  # Using 0.01 as the minimum distance threshold
    print(f"contact_points: {contact_points}")
    
    
    # Check the minimum distance
    if contact_points:
        
        min_distance = min([point[8] for point in contact_points])
        print(f"contact_distance: {min_distance}")
        if min_distance < 0.2:
            # Change the color of the robot arm to red
            p.changeVisualShape(jaka_id, -1, rgbaColor=[1, 0, 0, 1])
            p.changeVisualShape(rectangle_body_id, -1, rgbaColor=[1, 0, 0, 1])
    else:
        # Restore the color of the robot arm to blue
        p.changeVisualShape(rectangle_body_id, -1, rgbaColor=[0, 0, 1, 1])