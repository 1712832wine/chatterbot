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
    global last_message
    message = request.json['message']

    response = chatbot.get_response(message)
    response_messages = [{"success": True, "text": response.text}]

    if (response.text == 'Ồ, không phải hả. Sorry nha, Sa ngu ngốc quá.' and last_message):
        answer = googleSearch(last_message)
        response_messages.append({"success": True, "text": answer})

    last_message = message
    return jsonify(response_messages)


if __name__ == '__main__':
    last_message = ''
    app.run(debug=True)
