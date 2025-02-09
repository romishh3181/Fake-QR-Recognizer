import os
import cv2 as cv
from sklearn.model_selection import train_test_split
import numpy as np

realqr=r"D:\Fake QR Recognition\real_qr"
fakeqr=r"D:\Fake QR Recognition\fake_qr"
IMG_SIZE=128
X=[]
Y=[]

def preprocess_images(dir_path,label):
    images=os.listdir(dir_path)
    for img in images:
        imgpath=os.path.join(dir_path,img)
        imgn=cv.imread(imgpath,cv.IMREAD_GRAYSCALE)
        if imgn is not None:
            imgn=cv.resize(imgn,(IMG_SIZE,IMG_SIZE))
            X.append(imgn)
            Y.append(label)
preprocess_images(realqr,0)
preprocess_images(fakeqr,1)

X=np.array(X) / 255.0
X=np.expand_dims(X,axis=-1)
Y=np.array(Y)

print("Total images preprocessed: ",len(X))
X_train,X_temp,Y_train,Y_temp=train_test_split(X,Y,test_size=0.3,random_state=42,stratify=Y)
X_val,X_test,Y_val,Y_test=train_test_split(X_temp,Y_temp,test_size=0.5,random_state=42,stratify=Y_temp)

print(f"Train set: {len(X_train)} (70%) Test set: {len(X_test)} 15% Val Set: {len(X_val)} 15%")
np.savez("preprocessed_dt.npz",X_train=X_train,Y_train=Y_train,X_test=X_test,Y_test=Y_test,X_val=X_val,Y_val=Y_val)

