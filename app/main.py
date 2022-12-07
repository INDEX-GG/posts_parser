from fastapi import FastAPI, Depends
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.utils import read_from_json_file, get_post_item

app = FastAPI()

app.mount("/photo", StaticFiles(directory="photo"), name="photo")
app.mount("/files", StaticFiles(directory="files"), name="files")

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
        1: 'zapchasti774.json',
        2: 'zapchasti174.json',
        3: 'part-servis.json',
        4: 'instrument-oborudovanie.json',
        5: 'oborudovanie74.json',
        6: 'stroi-materialy74.json',
        7: 'stroimaterialy74.json',
        8: 'metallstanki74.json'
    }

    result = read_from_json_file(file_name=page_filters[params.page])
    return {'posts': result}


@app.get("/post")
async def post():
    result = read_from_json_file(file_name='zapchasti774.json')
    return {'posts': result}


@app.get("/post/{item_id}")
async def post_item(item_id):
    result = get_post_item(item_id)
    return {"post_item": result}
