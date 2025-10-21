from flask import Flask, request, jsonify
from firebase_admin import auth
from firebase_admin import credentials
from dotenv import load_dotenv
import firebase_admin
import json
import requests
import os

cred = credentials.Certificate("auth-firebase.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__)
load_dotenv()

def verify_token():
    id_token = request.headers.get('Authorization')
    if not id_token:
        return jsonify({'error': 'Token não fornecido'}), 401

    try:
        decoded_token = auth.verify_id_token(id_token)
        request.uid = decoded_token['uid']
    except auth.InvalidIdTokenError:
        return jsonify({'error': 'Token inválido'}), 401
    except auth.ExpiredIdTokenError:
        return jsonify({'error': 'Token expirado'}), 401
    

@app.before_request
def before_request_func():
    if request.endpoint not in ['login', 'signup']:
        return verify_token()

@app.route('/signup', methods=['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']

    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print(user.uid)
        return jsonify({'message': 'User created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={os.getenv('FIREBASE_API_KEY')}"

    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        return jsonify({'error': 'Credenciais inválidas'}), 401
    json_response = json.loads(response.text)
    return jsonify({
        'message': 'Login realizado com sucesso',
        'token': json_response['idToken'],
        'refreshToken': json_response['refreshToken']
    }), 200

@app.route('/endpoint_protegido', methods=['POST'])
def endpoint_protegido():
    return jsonify({'message': 'Acessando endpoint protegido'}), 200

if __name__ == '__main__':
    app.run(debug=True)