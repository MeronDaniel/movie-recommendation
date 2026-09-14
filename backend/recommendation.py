from flask import Blueprint, request, render_template
import requests
import json

recommendation_bp = Blueprint('recommendations', __name__)

OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama’s local endpoint

@recommendation_bp.route('/')
def form():
    return render_template('Recommendation.vue')  # Render the form template
           

@recommendation_bp.route('/ask', methods=['POST'])
def generate():
    #data = request.get_json()
    prompt = request.form.get("recommends", "")

    # Payload to be sent to Ollama
    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
    }
    

    response = requests.post(OLLAMA_URL, json=payload, stream=True)
    

    output = ""
    for line in response.iter_lines():
        if line:
            chunk = line.decode("utf-8")

            # Each line represents a JSON event streamed from Ollama
            try:
                chunk_json = json.loads(chunk) # json.load(c) converts each chunk into the proper JSON format required for processing.
                output += chunk_json.get("response", "") # We extract the 'response' key from the JSON payload, as it contains the actual text output from the model.
            except:
                pass

    return render_template('Recommendation.vue', response=output)
