import os 
import whisper
from flask import Flask, request, jsonify

app = Flask(__name__)

#Load  Whisper model (you can use "tiny", "base", "small", "medium", "large")
model = whisper.load_model("tiny")

@app.route('/healthcheck', methods=["GET"])
def healthcheck():
    return jsonify({"status": "ok"})






@app.route('/transcribe', methods=["Post"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    #save the file temporarily
    filepath = "temp.mp3"
    file.save(filepath)

    #run Whisper
    result = model.transcribe(filepath)

    #clean up
    os.remove(filepath)

    return jsonify({"text": result["text"]})

@app.route('/', methods=["GET"])
def home():
    return "Whisper Flask API is running!"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
