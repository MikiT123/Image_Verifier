import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from PIL import Image

app = Flask(__name__)
CORS(app)

model = pipeline("image-classification", model="microsoft/resnet-50")

@app.route("/analyze", methods=["POST"])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = Image.open(request.files['image'].stream).convert("RGB")
    result = model(image)[0]
    return jsonify({"label": result['label'], "confidence": float(result['score'])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
