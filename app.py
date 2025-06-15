from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# チャットボットのインスタンス作成
chatbot = ChatBot("MyBot")
trainer = ChatterBotCorpusTrainer(chatbot)

# 一度だけ英語コーパスでトレーニング
trainer.train("chatterbot.corpus.english")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    bot_response = chatbot.get_response(user_input)
    return jsonify(str(bot_response))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
