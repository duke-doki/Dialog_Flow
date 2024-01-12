# DialogFlow bot

A bot that responds to your messages in tg and vk.

## Environment


### Requirements

Python 3.10 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

### Environment variables

- TELEGRAM_TOKEN
- VK_TOKEN
- PROJECT_ID

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
TELEGRAM_TOKEN=684537...
PROJECT_ID=tg-bot...
VK_TOKEN=vk1.a.sF...
```

#### How to get

- Create a tg chatbot to get its token with [BotFather](https://telegram.me/BotFather). 

- Create a VK group and get its token [here](https://vk.com/club224221946?act=tokens).

- Follow the instructions to create your project [here](https://cloud.google.com/dialogflow/es/docs/quick/setup).


### create_intent

To create more intents, run:
```bash
python create_intent.py [json_file]
```
The file must look like the provided `questions.json`.

### Run

Launch on Linux(Python 3) or Windows:
```bash
python tg_dialogflow_bot.py
```
```bash
python vk_dialogflow_bot.py
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).