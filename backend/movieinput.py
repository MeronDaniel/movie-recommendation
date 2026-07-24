from flask import Flask, Blueprint, current_app, jsonify, request, requests
from werkzeug.security import generate_password_hash, check_password_hash
#from supabase import create_client
import os


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route('/movieinput', methods=['POST'])
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
        
        return jsonify({"movie": movie_data}), 201

