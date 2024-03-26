import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

API_TOKEN = ""


class Chat(BaseModel):
    id: int


class Message(BaseModel):
    chat: Chat
    text: str


class Update(BaseModel):
    update_id: int
    message: Message


app = FastAPI()


@app.on_event("startup")
def init():
    global API_TOKEN
    API_TOKEN = os.getenv('API_TOKEN')
    print(f'API_TOKEN = {API_TOKEN}')


@app.post("/translator_en_to_ru_bot")
def translator(update: Update):
    print(update)

    chat_id = update.message.chat.id
    text = update.message.text

    response = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage?&chat_id={chat_id}&text={text}'

    r = requests.get(response)
    print(r)

    return {"status": "success"}


@app.get("/")
def status():
    return {"status": "ok"}
