import configparser
import requests

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
OPENAI_KEY = config.get('open-ai', 'secret_key')
CHATGPT_URL = config.get('open-ai', 'url')


@ app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@ handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # model parameter
    data = {
        "model": "text-davinci-003",
        "prompt": event.message.text,
        "max_tokens": 4000,
        "temperature": 0.9,
        # "top_p": 1,
        # "n": 1,
        # "stream": False,
        # "logprobs": None,
        # "stop": "\n"
    }

    # API from open ai
    response = requests.post(
        CHATGPT_URL,
        headers={
            'Content-Type': 'application/json',
            'Authorization': " ".join(["Bearer", OPENAI_KEY])
        },
        json=data)

    res_json = response.json()
    reply_text = res_json.get("choices")[0].get(
        "text").replace("\n", "").replace("?", "")

    # Reply the text to client
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text))


if __name__ == "__main__":
    app.run()
