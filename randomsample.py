import random
import os
import shutil

newfkqrpath=r"D:\Fake QR Recognition\fake_qrs"
oldpth=r"D:\Fake QR Recognition\fake_qr"

os.makedirs(newfkqrpath,exist_ok=True)
images=os.listdir(oldpth)

rsamp=random.sample(images,10000)
for img in rsamp:
    shutil.copy(os.path.join(oldpth,img),os.path.join(newfkqrpath,img))