from fastapi import FastAPI

from app.utils import read_from_file

app = FastAPI()


@app.get('/posts')
async def get_posts():
    result = read_from_file(file_name='avito.txt')
    return {'posts': result}
