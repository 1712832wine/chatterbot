# This file is using python 3.9.8

from flask_cors import CORS
from flask import Flask, request, jsonify
from google_search import googleSearch
from trainer import chatbot

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/messages/send', methods=['POST'])
def sendmessage():
    threshold = 0.75
    message = request.json['message']
    response = chatbot.get_response(message)
    if response.confidence >= threshold:
        response_messages = [{"success": True, "text": response.text}]
    else:
        answer = googleSearch(message)
        response_messages = [{"success": True, "text": answer}]
    return jsonify(response_messages)


if __name__ == '__main__':
    app.run(debug=True)
