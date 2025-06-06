import random
import logging

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/number")
def handle_number():
    number = random.randint(0, 256)
    logging.info(f"Returning number: {number}")
    return PlainTextResponse(str(number))
