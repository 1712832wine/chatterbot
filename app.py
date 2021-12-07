# This file is using python 3.9.8

from flask_cors import CORS
from flask import Flask, request, jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
CORS(app)

conversation = [
    "Xin chào",
    "Chào bạn",
    "Bạn đang làm gì đó?",
    "Tôi đang học",
    "Nghe tuyệt đó",
    "Cảm ơn",
    "Không có chi"
]
# Create chatbot
chatbot = ChatBot("Ron Obvious",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
# train
trainer = ListTrainer(chatbot)
trainer.train(conversation)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/messages/send', methods=['POST'])
def sendmessage():
    message = request.json['message']
    response_message = chatbot.get_response(message)
    print("response_message",response_message)
    return jsonify({"success": True, "response_message": str(response_message)})


if __name__ == '__main__':
    app.run(debug=True)
