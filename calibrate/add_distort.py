from wand.image import Image
import numpy as np
import cv2

with Image(filename='/home/fan/Surgical-robot/data/aruco/20231206-223610.jpg') as img:
    print(img.size)
    img.virtual_pixel = 'transparent'
    img.distort('barrel', (0.1, 0.0, 0.0, 1.0)) # play around these values to create distortion
    img.save(filename='filname.png')
    # convert to opencv/numpy array format
    img_opencv = np.array(img)

# display result with opencv
cv2.imshow("BARREL", img_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()