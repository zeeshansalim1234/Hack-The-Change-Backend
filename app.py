from firebase_admin import credentials, initialize_app, firestore
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS

db = firestore.client()
user_Ref = db.collection('user')

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def input():

    return render_template('index.html')

@app.route('/getSample', methods = ['GET'])
def sample():

    test = {"name": "Zeeshan"}
    return jsonify(test)

if __name__ == "__main__":
    app.run(debug=True)
    