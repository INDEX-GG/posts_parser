from fastapi import FastAPI, Depends
from pydantic import BaseModel

from app.utils import read_from_file, read_from_json_file, get_post_item
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


class Posts(BaseModel):
    page: int | None = 1


@app.get('/posts')
async def get_posts(params: Posts = Depends()):
    page_filters = {
        1: 'yandex.txt',
        2: 'yandex2.txt',
        3: 'yandex3.txt',
        4: 'tor.json',
        5: 'zoom.json',
        6: 'stroika.json',
        7: 'stroika2.json'
    }
    if params.page == 4 or params.page == 5 or params.page == 6 or params.page == 7:
        result = read_from_json_file(file_name=page_filters[params.page])
    else:
        result = read_from_file(file_name=page_filters[params.page])
    return {'posts': result}


@app.get("/post")
async def post():
    result = read_from_file(file_name='yandex.txt')
    return {'posts': result}


@app.get("/post/{item_id}")
async def post_item(item_id):
    result = get_post_item(item_id)
    return {"post_item": result}
