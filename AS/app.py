from flask import Flask, request, jsonify, send_file, render_template
from agent import generate_dataset
from exporter import parse_response, export
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    filename = data.get("filename", "dataset")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    # Get response from Ollama via agent
    raw_response = generate_dataset(prompt)
    
    # Parse the response
    parsed = parse_response(raw_response)
    
    if not parsed:
        return jsonify({"error": "Failed to parse dataset"}), 500
    
    # Export to all formats
    paths = export(parsed, filename)
    
    return jsonify({
        "success": True,
        "preview": parsed,
        "files": paths
    })

@app.route("/download/<format>/<filename>")
def download(format, filename):
    path = f"outputs/{filename}.{format}"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)