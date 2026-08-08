from flask import Blueprint, jsonify, request
import requests
import os

movieinput_bp = Blueprint("movieinput", __name__, url_prefix="/api/movieinput")

@movieinput_bp.route('/search', methods=['POST'])
def search():

    if request.method == 'POST':
        data = request.get_json()
        movie = data.get('movie')
        

        if not movie:
            return jsonify({"error": "Movie is required"}), 400        

        OMDB_KEY = os.getenv("OMDB_KEY")
          
        response = requests.get(f"http://www.omdbapi.com/?t={movie}&apikey={OMDB_KEY}")

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch movie data"}), 400

        

        movie_data = response.json()

        if movie_data.get("Response") == "False":
            return jsonify({"error": "Movie not found"}), 404
        
        return jsonify({"movie": movie_data}), 200

