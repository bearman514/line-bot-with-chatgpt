# Line Bot with ChatGPT

Using Python to create a Line Bot script with ChatGPT from OpenAI.

> **Short introduction from ChatGPT blog:**
> Optimizing Language Models for Dialogue. ChatGPT can answer followup questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests.

## Table of Contents

- [Screenshots](#screenshots)
- [How to Use?](#how-to-use)
  - [Setup](#0-setup)
  - [Get tokens](#1-get-tokens)
  - [Modify config](#2-modify-config)
  - [Run Flask](#3-run-flask)
  - [Deploy](#4-deploy)
  - [Start to chat!](#5-start-to-chat)
- [Reference](#reference)

## Screenshots

![screenshots.jpg](https://github.com/bearman514/line-bot-with-chatgpt/blob/main/images/screenshot.jpg)

## How to Use?

#### 0. Setup
Suggest for create a `venv` by virtualenv
```
git clone https://github.com/bearman514/line-bot-with-chatgpt.git
pip install -r requirements.txt
```

#### 1. Get Tokens

- Login in LINE Developers
    - Create a Messaging API channel
    - Get `Channel access token` at Messaging API (Press issue button to get it)
    - Get `Channed secret` at Basic settings 

- Apply an `API keys` on OpenAI (See at [Reference](#reference))

#### 2. Modify config
- Paste the tokens inside the config file: [config.ini](https://github.com/bearman514/line-bot-with-chatgpt/blob/main/config.ini)

#### 3. Run Flask
- Localhost with port 5000
    ```python .\app.py```

#### 4. Deploy
- If you have public IP, deploy with it!  (I suppose you know how to do it.)
- If not, try to use `ngrok` for getting LINE Bot `Webhook`.
    - [Install ngrok](https://ngrok.com/download)
    - Add authtoken (Sign up on ngrok to get the token)
        `ngrok config add-authtoken <token>`
    - Start a tunnel
        `ngrok http 5000`
    - Paste the URL from ngrok to LINE Bot `Webhook URL` 
        - ngrok 
            - Find URL (Cloud Edge > Endpoints)
        - LINE Developers
            - Find the place `Webhook URL` (Messaging API > Webhook settings > Webhook URL)
            - Paste `https://<the-link-from-ngrok>/callback`
            - Press `Verify` and open `Use webhook`

#### 5. Start to chat!
- Find the chat bot on LINE, talk to ChatGPT!

## Reference

- OpenAI
  - [API Reference](https://beta.openai.com/docs/api-reference/introduction)
  - [Create API keys](https://beta.openai.com/account/api-keys)
  - [Model GPT-3](https://beta.openai.com/docs/models/gpt-3)
  - [ChatGPT: Optimizing Language Models for Dialogue](https://openai.com/blog/chatgpt/)
- LineBot
  - [LINE Developers](https://developers.line.biz/en/)
  - [Getting started with the Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/#page-title)
  - [How Messaging API works](https://developers.line.biz/en/docs/messaging-api/overview/#how-messaging-api-works)
- Deployment
  - [Install ngrok](https://ngrok.com/download)
