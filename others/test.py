import pybullet as p
import pybullet_data
import time
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)  # Gravity in earth

planeID = p.loadURDF("plane.urdf")

euler_angles = [0,0,0]  # Original angles
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0,0,1]  # Original position

robotId = p.loadURDF("robots/robot.urdf.xacro", startPosition, startOrientation)



for i in range (10000):
    

    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()