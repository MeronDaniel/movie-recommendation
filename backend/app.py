#Initializing Flask app

from flask import Flask, render_template, request, jsonify
from supabase import create_client
from auth import auth_bp
from dotenv import load_dotenv
import os

load_dotenv()



def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    @app.route('/')
    def home():
        return jsonify({"status": "Backend running"})

    app.register_blueprint(auth_bp)
    app.supabase = supabase
    return app

#@app.route('/')
#def home():
#    return "Welcome to the Flask app!"

#@app.route('/login', methods=['GET'])
#def login():
#    return render_template('Login.vue')

#@app.route('/register', methods=['GET'])
#def register():
#    return render_template('Register.vue')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)