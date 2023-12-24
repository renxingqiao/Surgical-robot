import numpy as np
import cv2
import dlib
import time

def get_detector():
    detector = dlib.get_frontal_face_detector()  
    predictor = dlib.shape_predictor('/home/fan/Surgical-robot/utils/shape_predictor_68_face_landmarks.dat')  
    return detector, predictor
# a function to detect the face
def face_detect_from_img(img_path):
    if isinstance(img_path, str):
        img_color = cv2.imread(img_path)
    else: img_color = img_path
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # result_img = np.zeros([height, width, 3], dtype=np.uint8)

    
    rects = detector(img_gray, 0)

    
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img_color,rects[i]).parts()])
        
        for idx, point in enumerate(landmarks):
            
            pos = (point[0, 0], point[0, 1])
            
            cv2.circle(img_color, pos, 2, (0, 0, 255), -1)

    
    # landmarks = landmarks.tolist()
    # extract_idx = [36, 39, 42, 45, 27, 28, 29, 30, 31, 33, 35, 48, 50, 52, 54, 56, 58]
    # for idx in extract_idx:
    #     cv2.circle(img, landmarks[idx], 2, (0, 0, 255, -1))

    cv2.imshow("result", img_color)
    # cv2.imwrite("/home/fan/Surgical-robot/paper_pictures/face/output.png",img_color)
    # cv2.resizeWindow("result", 640, 480)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def face_detect_from_camera_pc():

    capture = cv2.VideoCapture(0)

    while(True):
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)

        face_detect_from_img(frame)

        c = cv2.waitKey(10)
        if c == 27:
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__=='__main__':

    detector, predictor = get_detector()

    # 利用单张图片预测
    img_path = "/home/fan/Surgical-robot/paper_pictures/face/data_3.png.png"
    # face_detect_from_img(img_path)
    # img = cv2.imread("/home/fan/face68/data_image/out/2022_08_16_15_47_31/color/2.png")
    
    # tic = time.perf_counter()
    # face_detect_from_img(img_path)
    # toc = time.perf_counter()
    # print("the detection use time is %sms"%((toc - tic) * 1000) )
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 使用相机预测
    face_detect_from_camera_pc()

