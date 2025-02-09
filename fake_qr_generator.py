import cv2 as cv
import os
import numpy as np
import random
pathtorealimg=r"D:\Fake QR Recognition\real_qr"
pathtofake=r"D:\Fake QR Recognition\fake_qr"
cnt=0
def genfake(img,path2):
    imag=cv.imread(img)
    fate=random.randint(1,5)
    if fate==1:
        blurred=cv.GaussianBlur(imag,(5,5),0)
        cv.imwrite(f"{path2}/fakeimg_{++cnt}",blurred)
    elif fate==2:
        noise=np.random.normal(0,25,imag.shape).astype(np.uint8)
        noisyimage=cv.add(imag,noise)
        cv.imwrite(f"{path2}/fakeimg_{++cnt}",noisyimage)
    elif fate==3:
        rows, cols, ch = imag.shape
        pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
        pts2 = np.float32([[30, 60], [220, 40], [70, 220]])
        M = cv.getAffineTransform(pts1, pts2)
        distorted = cv.warpAffine(imag, M, (cols, rows))
        cv.imwrite(f"{path2}/fakeimg_{++cnt}",distorted)
    else:
        center = (imag.shape[1] // 2, imag.shape[0] // 2)
        angle = 30
        scale = 1
        rotationmat=cv.getRotationMatrix2D(center,angle,scale)
        rotatedimg=cv.warpAffine(imag,rotationmat,(imag.shape[1],imag.shape[0]))
        cv.imwrite(f"{path2}/fakeimg_{++cnt}",rotatedimg)
for img in pathtorealimg:
    if os.path.isfile(os.path.join(pathtorealimg,img)):
        genfake(os.path.join(pathtorealimg,img),pathtofake)




