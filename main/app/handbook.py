from flask import Flask, render_template, send_from_directory
from flask import Flask, render_template, request, send_file, jsonify
import skimage
from PIL import Image
import numpy as np
import io
import os
import requests

app = Flask(__name__)

# Route to serve the handbook page
@app.route('/')
def handbook():
    return render_template('handbook.html')

# Route to serve other HTML files
@app.route('/templates/<path:filename>')
def other_html(filename):
    if filename.endswith('.html'):
        return send_from_directory('templates', filename)
    else:
        return "File not found", 404

# Route to serve images
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('static/images', filename)

@app.route("/askGPT", methods=['POST'])
def chatGPT():
    def chatGPT(ques):
        url = "https://chatgpt-api8.p.rapidapi.com/"

        payload = [
            {
                "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
                "role": "system"
            },
            {
                "content": f"{ques}",
                "role": "user"
            }
        ]
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "030c80dc47mshbe06ccceee3100cp18b554jsnc6867b4f1b65",
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
        }
        # huytrongnghia: 8dd3bfa3f3mshda3845149bb330ep1c4505jsna147eee499b5
        # khkt: d89a8977f9mshd28e97843a01cf2p158370jsn0cb69019b238
        # huynghia: 8eacc0c16dmshb79a0fe65bc3344p14e02ajsn29bf84e2e8b9
        # huytrong: 030c80dc47mshbe06ccceee3100cp18b554jsnc6867b4f1b65
        # nguyenquynh: 0c6c1ec218msh58fce662b00a268p1e2172jsn77027176568f

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        return data["text"]

    try:
        data = request.json
        user_message = data['message']

        # Call your ChatGPT function here
        bot_message = chatGPT(user_message)

        return jsonify({'content': bot_message})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

   
# cấu trúc thư mục:
# app/
# ├── backend.py 
# ├── static/                        
# │   ├── style.css                  
# │   └── script.js      
# │   └── images/               
# └── templates/                     
#     └── handbook.html 
#     └── acne.html                