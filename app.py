# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from PIL import Image

app = Flask(__name__)
CORS(app)  # Allow requests from frontend (for GitHub Pages or any origin)

# Public model for testing purposes
model = pipeline("image-classification", model="microsoft/resnet-50")

@app.route("/analyze", methods=["POST"])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        image = Image.open(request.files['image'].stream).convert("RGB")
        result = model(image)[0]  # Take top prediction
        return jsonify({
            "label": result['label'],
            "confidence": float(result['score'])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
