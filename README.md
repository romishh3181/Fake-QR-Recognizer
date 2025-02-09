# 🚀 AI-Based QR Code Spoofing Detection

## 📌 Overview

QR code spoofing is a growing security threat where fake QR codes are used to deceive users. This project leverages **Computer Vision** and **Deep Learning (CNNs)** to detect fake QR codes and protect users from potential scams.

## 🔥 Features

✅ **Real vs. Fake QR Code Detection** - Uses a CNN-based model to classify QR codes. ✅ **Web Interface** - Users can upload a QR code image for real-time analysis. ✅ **Flask API** - Backend for handling image uploads and running the model. ✅ **JavaScript (AJAX) Integration** - Provides instant feedback on the prediction. ✅ **Dataset Handling** - Uses a combination of real and malicious QR codes.

## 🏗️ Tech Stack

- **Python** (Flask, OpenCV, TensorFlow/Keras)
- **JavaScript** (AJAX for frontend-backend communication)
- **HTML & CSS** (Frontend UI)
- **Git & GitHub** (Version control)

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Fake-QR-Recognizer.git
cd Fake-QR-Recognizer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## 🖼️ Web Interface Preview

The web interface allows users to **upload a QR code image** and get an **instant prediction** on whether it's fake or real.

## 📊 Dataset

- **Real QR Codes**: `10,000` images
- **Fake QR Codes**: `10,000` images (various attack methods: noise, distortion, overlay, blurring)
- **Format**: `.png`, `.jpg`
- **Size**: Preprocessed for model training

## 🔑 Key Learnings

✅ Applied **CNNs** for image classification ✅ Implemented **Flask API** for seamless backend processing ✅ Built an interactive **frontend** using JavaScript & AJAX ✅ Managed **large datasets** efficiently

## 📜 License

This project is licensed under the **MIT License**.

---

### 🎯 Future Improvements

🔹 Improve dataset diversity for better accuracy\
🔹 Deploy the model as a public API for easy integration\
🔹 Add mobile compatibility for on-the-go QR scanning

📩 **Have feedback or suggestions? Feel free to contribute!** 😊

