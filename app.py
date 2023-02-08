import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template

app = Flask(__name__)

pairs = [
  [
    r"My name is (.*)",
    ["Hello %1, how are you today?, hey %1 %1 how's GHW going?"]
],
    [
    r"What is your name?",
    ["My name is gene", "I'm the cutest GHW gene bot",
        "It's nice to meet you I'm gene"]
],
    [
    r"sorry (.*)",
    ["It's alright", "Never gonna give you up"]
],
    [
    r"Hey, I'm rick",
    ["Go away", "I will give you up"]
],
    [
    r"Quit",
    ["Bye it was great talking to you", "See you soon"]
],
[
    r"What categories are there in GHW?",
    ["There are many categories and they can be found here"]
],
]

chatbot = Chat(pairs, reflections)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["text"]
    response = chatbot.respond[message]
    return response


if __name__ == "__main__":
    app.run()
