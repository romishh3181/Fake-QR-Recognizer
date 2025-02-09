import cv2
import numpy as np
import tensorflow as tf

IMG_SIZE = 128
model = tf.keras.models.load_model("qr_model.h5")

def predict_qr(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) / 255.0
    img = np.expand_dims(img, axis=(0, -1))  

    prediction = model.predict(img)[0][0]
    return "Fake QR Code" if prediction > 0.5 else "Real QR Code"

image_path = r"D:\Fake QR Recognition\real_qr\1011-v1.png"
result = predict_qr(image_path)
print(f"QR Code Prediction: {result}")
