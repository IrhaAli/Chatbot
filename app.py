from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Route to the chat page


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_message = requests.args.get('msg')
    api_key = "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"
    model = "text-davinci-003"
    response = generate_response_gpt3(user_message, model, api_key)
    return response


def generate_response_gpt3(user_messages, model, api_key):
    prompt = (f"User: {user_messages}\n"
              f"ChatBot:")
    response = requests.post(
        "https://api.openapi.com/v1/engines/text-davinci-003/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "prompt": prompt,
            "max_tokens": 200,
            "temperature": 0.7,
        }
    ).json()
    return response('choices')[0]["text"].strip()[len(prompt):]


# Run the app
if __name__ == "__main__":
    app.run()
