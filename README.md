# 🧠 Toxic Comment Detection System

## 🔍 Overview
The **Toxic Comment Detection System** is an AI-powered web application that identifies toxic and hate speech in real-time. It uses a fine-tuned BERT model to predict the toxicity of user-input text and displays results instantly. The system also includes a **Chrome Extension** that blurs out toxic comments on social media platforms such as YouTube and Instagram.

---

## 🚀 Live Preview
### 🌐 Try it Online:
  🔗 https://toxic-comment-detector-doqs.onrender.com
### 💻 Download Chrome Extension ZIP:
  Click the button on the landing page or use https://drive.google.com/file/d/1tlcMZA7iFqsEo9a8n_oIAsJvzbtq2OAp/view?usp=drive_link to download the extension .zip file.

---

## 🧩 How to Use the Chrome Extension Locally

1. **Download** and **unzip** the extension ZIP file.
2. Open **Google Chrome** and go to `chrome://extensions/`.
3. Turn on **Developer Mode** (top right).
4. Click **"Load unpacked"**.
5. Select the **unzipped folder** of the extension.
6. Extension is now added and will automatically blur toxic comments on supported platforms.

---

## 🛠️ Tech Stack

| Layer      | Technology                |
|------------|---------------------------|
| Frontend   | React.js, HTML, CSS       |
| Backend    | Flask (Python)            |
| ML Model   | BERT (`transformers`, `tensorflow`) |
| Browser Extension | JavaScript, Manifest v3      |

---

## 🚀 Features
- Real-time comment toxicity detection with high accuracy.
- Web UI for checking individual comments.
- Chrome Extension that detects and blurs toxic comments automatically.
- Probability score of toxicity with intuitive feedback.
- Custom fine-tuned BERT model hosted via Flask backend.

---

## 🌐 Usage
### 🌍 Web App
- Enter any text or comment into the input box.
- Click Check Toxicity.
- You'll see the prediction label (toxic/non-toxic) and confidence score.

### 🧩 Extension
- Visit YouTube or Instagram.
- Toxic comments will be blurred automatically.
- You can also unhide the blurred comment on your wish.

---

## 📚 Acknowledgments
- Hugging Face 🤗 for BERT
- Flask for serving my ML Model
- React.js for frontend
- Google Chrome for extension support
