
import numpy as np
import time
import cv2
import cv2.aruco as aruco
from detect_single_aruco import detect_single_frame

#相机内参矩阵
mtx = np.array([
        [1220.69,       0, 661.20],
        [      0, 1176.19, 281.00],
        [      0,       0,      1],
        ])

dist = np.array( [-4.76531264e-02, 8.98268556e-02, 8.77978795e-04, 1.08441766e-02, 9.03702693e-01] )


if __name__ == '__main__':

    cap = cv2.VideoCapture(4)

    #num = 0
    while True:
        ret, frame = cap.read()

        detect_single_frame(frame, mtx, dist, save=False, show=True, show_delay=10)
    
    cv2.destroyAllWindows()
    
