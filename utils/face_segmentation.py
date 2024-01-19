import os.path as osp
import os
import numpy as np
import cv2
import dlib


def face_detect_from_img(img_path):
    if isinstance(img_path, str):
        img_color = cv2.imread(img_path)
    else: img_color = img_path
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # result_img = np.zeros([height, width, 3], dtype=np.uint8)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('/home/caoyicong/workspace/Surgical-robot/utils/shape_predictor_68_face_landmarks.dat')    
    rects = detector(img_gray, 0)

    
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img_color,rects[i]).parts()])
        
        for idx, point in enumerate(landmarks):
            
            pos = (point[0, 0], point[0, 1])
            
            cv2.circle(img_color, pos, 2, (0, 0, 255), -1)
    return img_color
    # cv2.imshow("result", img_color)


def get_image_hull_mask(image_shape, image_landmarks, ie_polys=None):
    # get the mask of the image
    if image_landmarks.shape[0] != 68:
        raise Exception(
            'get_image_hull_mask works only with 68 landmarks')
    int_lmrks = np.array(image_landmarks, dtype=np.int32)

    #hull_mask = np.zeros(image_shape[0:2]+(1,), dtype=np.float32)
    hull_mask = np.full(image_shape[0:2] + (1,), 0, dtype=np.float32)

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[0:9],
                        int_lmrks[17:18]))), (1,))

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[8:17],
                        int_lmrks[26:27]))), (1,))

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[17:20],
                        int_lmrks[8:9]))), (1,))

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[24:27],
                        int_lmrks[8:9]))), (1,))

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[19:25],
                        int_lmrks[8:9],
                        ))), (1,))

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[17:22],
                        int_lmrks[27:28],
                        int_lmrks[31:36],
                        int_lmrks[8:9]
                        ))), (1,))

    cv2.fillConvexPoly(hull_mask, cv2.convexHull(
        np.concatenate((int_lmrks[22:27],
                        int_lmrks[27:28],
                        int_lmrks[31:36],
                        int_lmrks[8:9]
                        ))), (1,))

    # nose
    cv2.fillConvexPoly(
        hull_mask, cv2.convexHull(int_lmrks[27:36]), (1,))

    if ie_polys is not None:
        ie_polys.overlay_mask(hull_mask)
    print()
    return hull_mask

# 加入alpha通道 控制透明度
def merge_add_alpha(img_1, mask):
    # merge rgb and mask into a rgba image
    r_channel, g_channel, b_channel = cv2.split(img_1)
    if mask is not None:
        alpha_channel = np.ones(mask.shape, dtype=img_1.dtype)
        alpha_channel *= mask*255
    else:
        alpha_channel = np.zeros(img_1.shape[:2], dtype=img_1.dtype)
    img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    return img_BGRA

def merge_add_mask(img_1, mask):
    if mask is not None:
        height = mask.shape[0]
        width = mask.shape[1]
        channel_num = mask.shape[2]
        for row in range(height):
            for col in range(width):
                for c in range(channel_num):
                    if mask[row, col, c] == 0:
                        mask[row, col, c] = 0
                    else:
                        mask[row, col, c] = 255

        r_channel, g_channel, b_channel = cv2.split(img_1)
        r_channel = cv2.bitwise_and(r_channel, mask)
        g_channel = cv2.bitwise_and(g_channel, mask)
        b_channel = cv2.bitwise_and(b_channel, mask)
        res_img = cv2.merge((b_channel, g_channel, r_channel))
    else:
        res_img = img_1
    return res_img

def get_landmarks(image):

    predictor = '/home/caoyicong/workspace/Surgical-robot/utils/shape_predictor_68_face_landmarks.dat'
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor)
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    rects = detector(img_gray, 0)
    landmarks = None  # 初始化landmarks为None
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(image, rects[i]).parts()])
    return landmarks


def get_seg_face(image):
    if image is not None:
        # 将BGR图像转换为RGB图像，因为Dlib使用RGB格式
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        landmarks = get_landmarks(image_rgb)
        if landmarks is not None:
            mask = get_image_hull_mask(image.shape, landmarks).astype(np.uint8)
            image_68pionts = face_detect_from_img(image)
            if image_68pionts is not None and image_68pionts.size > 0:
                cv2.imshow("result", image_68pionts)
            else:
                print("image_68points is empty or invalid.")          


            image_bgra = merge_add_alpha(image_rgb, mask)
            cv2.imshow("result1", image_bgra)

            image_bgr = merge_add_mask(image_rgb, mask)
            cv2.imshow("result2", image_bgr)
            cv2.waitKey(1)  # 如果你想要在窗口中看到结果，需要这个等待
        else:
            print("No landmarks detected.")
    else:
        print("Invalid image input.")


def face_seg_from_camera_pc():
    # 打开摄像头
    capture = cv2.VideoCapture(2)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)

        # 对摄像头实时画面应用人脸分割
        get_seg_face(frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    capture.release()
    cv2.destroyAllWindows()


def face_detect_from_camera_pc():
    # 打开摄像头
    capture = cv2.VideoCapture(2)

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        # 按 'ESC' 键退出
        if cv2.waitKey(1) & 0xFF == 27:
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    face_detect_from_camera_pc()



