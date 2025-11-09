# app.py
from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image

app = Flask(__name__)

# Public model for testing. Replace with a legit AI-detection model later
model = pipeline("image-classification", model="microsoft/resnet-50")

@app.route("/analyze", methods=["POST"])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = Image.open(request.files['image'].stream).convert("RGB")
    result = model(image)[0]  # Top prediction
    return jsonify({
        "label": result['label'],
        "confidence": float(result['score'])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
