from flask import Blueprint, jsonify, request
import requests
import os

display_bp = Blueprint("display", __name__, url_prefix="/api/display")

@display_bp.route('/<string:movie_title>/search', methods=['GET'])
def search(movie_title):

    if request.method == 'GET':
        OMDB_KEY = os.getenv("OMDB_KEY")

        response = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_KEY}")

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch movie data"}), 400

        movie_data = response.json()

        poster_url = movie_data.get("Poster")

        
        return jsonify({"poster_url": poster_url, "movie_title": movie_data.get("Title")}), 200

