#Initializing Flask app

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

def login():
    return render_template('Login.vue')

if __name__ == '__main__':
    app.run(debug=True)