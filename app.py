from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS
from predict import predict_comment
import os

app = Flask(__name__)
# CORS(app)

# Allow requests from any origin (frontend, browser, extension)
# CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Text input is missing"}), 400

    print("🔍 Received text:", data["text"])
    result = predict_comment(data["text"])
    print("✅ Sending result:", result)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses dynamic port
    app.run(debug=False, host='0.0.0.0', port=port)





# from flask import render_template
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from predict import predict_comment

# app = Flask(__name__)
# CORS(app)

# @app.route("/")
# def home():
#     return render_template("index.html")

# # More specific CORS configuration
# CORS(app, origins=[
#     "chrome-extension://*",
#     "http://localhost:3000",  # for your React app
#     "http://127.0.0.1:3000"
# ])

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     text = data.get("text", "")
#     if not text:
#         return jsonify({"error": "Text input is missing"}), 400
    
#     result = predict_comment(text)
#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5000)

# @app.route('/predict', methods=['POST'])
# def predict_api():
#     data = request.get_json()
#     print("🔍 Received text:", data)
#     result = predict_comment(data["text"])
#     print("✅ Sending result:", result)
#     return jsonify(result)










# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from predict import predict_comment  # your BERT prediction logic

# app = Flask(__name__)
# CORS(app)  # enable CORS

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     text = data.get("text", "")
#     if not text:
#         return jsonify({"error": "Text input is missing"}), 400
    
#     result = predict_comment(text)
#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True)
