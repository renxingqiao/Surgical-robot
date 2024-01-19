
import numpy as np
import time
import cv2
import os
import cv2.aruco as aruco
import time

mtx = np.array([
        [1220.69,       0, 661.20],
        [      0, 1176.19, 281.00],
        [      0,       0,      1],
        ])


dist = np.array( [-4.76531264e-02, 8.98268556e-02, 8.77978795e-04, 1.08441766e-02, 9.03702693e-01] )


def detect_single_frame(img, mtx, dist, save=False, show=False, font=cv2.FONT_HERSHEY_SIMPLEX, show_delay=10):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 加载ArUco字典
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

    # 创建ArUco检测器
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,
                                                        aruco_dict,
                                                        parameters=parameters)

    if ids is not None:
        # 计算位姿
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.2, mtx, dist)
        # Estimate pose of each marker and return the values rvet and tvec---different
        # from camera coeficcients
        (rvec-tvec).any() # get rid of that nasty numpy value array error


        for i in range(rvec.shape[0]):
            aruco.drawAxis(img, mtx, dist, rvec[i, :, :], tvec[i, :, :], 0.03)
            aruco.drawDetectedMarkers(img, corners)
        
        cv2.putText(img, "Id: " + str(ids), (0,40), font, 0.5, (0, 0, 255),1,cv2.LINE_AA)
        cv2.putText(img, "rvec: " + str(rvec[i, :, :]), (0, 60), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img, "tvec: " + str(tvec[i, :, :]), (0,80), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)


    else:
        ##### DRAW "NO IDS" #####
        cv2.putText(img, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)


    # import pdb;pdb.set_trace()

    if save:
        filename = f"result_{time.time()}.png"
        save_path = os.path.join('paper_pictures/aruco', filename)
        cv2.imwrite(save_path, img)
    
    if show:
        cv2.imshow('Camera Output', img)

        # 检测按键，如果是'q'则退出循环
        cv2.waitKey(show_delay)


if __name__ == '__main__':
    img = cv2.imread('../data/aruco.jpg')
    detect_single_frame(img, mtx, dist, save=False, show=False, show_delay=10)

