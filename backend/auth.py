from flask import Flask, Blueprint, current_app, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
#from supabase import create_client
import re
import os


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
        
    # Check if user exists
    supabase = current_app.supabase

    if request.method == 'GET':
 
        # Check if user exists
        supabase = current_app.supabase
 
        response = supabase.table("users").select("*").execute() #selects all users from the database, if it returns data, then user exists

        return jsonify(response.data), 200
    
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        confirmPassword = data.get('confirmPassword')

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({"error": "Invalid email format"}), 400

        if password != confirmPassword:
            return jsonify({"error": "Passwords do not match"}), 400
        

        existing = supabase.table("users").select("*").eq("email", email).execute() #checks based on specific email if user exists in database, if it does, return error message
        if existing.data:
            return jsonify({"error": "Email already registered"}), 400
        

        hashed = generate_password_hash(password)

        supabase.table("users").insert({
            "email": email,
            "hash_password": hashed
        }).execute()

        return jsonify({"message": "User registered successfully!"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():

    supabase = current_app.supabase


    if request.method == 'POST':

        """Login with email and password"""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Find user by email
        existing = supabase.table("users").select("*").eq("email", email).execute()

        if not existing.data:
            return jsonify({'error': 'Invalid email or password'}), 401
        
        #checks to compare password inputed to hash_password stored in database
        users = existing.data[0]

        if not check_password_hash(users['hash_password'], password):
            return jsonify({'error': 'Invalid email or password'}), 401

        return jsonify({
            'message': 'Login successful'
        }), 200
