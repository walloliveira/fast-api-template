from fastapi import FastAPI
import database

api = FastAPI()


@api.get('/')
async def get():
    return {
        'hello': 'world'
    }
