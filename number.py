from fastapi import FastAPI
import random
from ratelimit import limits,sleep_and_retry

one_minute=60
app = FastAPI()


@app.get('/get_number')
@sleep_and_retry
@limits(calls=5,period=one_minute)
def numbers():
    return random.randint(1,100)
