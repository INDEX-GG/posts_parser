from fastapi import FastAPI

from app.utils import read_from_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/posts')
async def get_posts():
    result = read_from_file(file_name='avito.txt')
    return {'posts': result}
