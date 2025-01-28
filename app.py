from flask import Flask, request, jsonify
import os
from datetime import datetime
import requests

app = Flask(__name__)

# Speicherpfad
storage_path = "/storage"
localai_url = os.getenv("LOCALAI_API_URL", "http://localai:8080/v1/images")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image = request.files['image']
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{image.filename}"
    file_path = os.path.join(storage_path, filename)
    
    # Speichere das Bild lokal
    os.makedirs(storage_path, exist_ok=True)
    image.save(file_path)
    
    # Sende das Bild an LocalAI
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(localai_url, files={"file": f})
        if response.status_code == 200:
            return jsonify({"message": "Image saved and forwarded", "localai_response": response.json()})
        else:
            return jsonify({"error": "Failed to forward image to LocalAI", "status_code": response.status_code}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    os.makedirs(storage_path, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
