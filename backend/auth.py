from flask import Flask, Blueprint, current_app, jsonify, request
from werkzeug.security import generate_password_hash
#from supabase import create_client
import re
import os


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")
#supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

#class User(db.Model):
 #   __tablename__ = 'users'
  #  id = db.Column(db.Integer, primary_key=True, nullable=False)
   # email = db.Column(db.String(255), unique=True, nullable=False)
    #hash_password = db.Column(db.String(255), nullable=True) #password shouldn't be stored in database, but as a hash using byrpt or werkzeug.security


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
 
        # Check if user exists
        supabase = current_app.supabase
 
        #response = supabase.table("users").select("*").eq("email", email).execute()
        response = supabase.table("users").select("*").execute()

        return jsonify(response.data), 200
    
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email format"}), 400

        if password != confirm_password:
            return jsonify({"error": "Passwords do not match"}), 400
        


    # Check if user exists
    supabase = current_app.supabase

    #response = supabase.table("users").select("*").eq("email", email).execute()
    response = supabase.table("users").select("*").execute()
    if response.data:
        return jsonify({"error": "Email already registered"}), 400
    

    hashed = generate_password_hash(password)

    supabase.table("users").insert({
        "email": email,
        "hash_password": hashed
    }).execute()

    return jsonify({"message": "User registered successfully!"}), 201

