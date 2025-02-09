from flask import Flask,request,Response,render_template,jsonify
import cv2 as cv
import numpy as np
import tensorflow as tf
import os

app=Flask(__name__)
model=tf.keras.models.load_model('qr_model.h5')

folderup="static/uploads"
app.config["Upload_folder"]=folderup
os.makedirs(folderup,exist_ok=True)
def predictqr(imgpath):
    img=cv.imread(imgpath,cv.IMREAD_GRAYSCALE)
    img=cv.resize(img,(128,128))/255.0
    img=np.expand_dims(img,axis=(0,-1))

    prediction=model.predict(img)[0][0]
    return "Fake QR Code" if prediction>0.5 else "Real QR Code"
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/upload",methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file found"}),400
    file=request.files["file"]
    if file.filename=="":
        return jsonify({"error":"No file selected"}),400
    filepath=os.path.join(app.config['Upload_folder'],file.filename)
    file.save(filepath)
    result=predictqr(filepath)
    return jsonify({"result":result,"image_url":filepath})
if __name__=="__main__":
    app.run(debug=True)

