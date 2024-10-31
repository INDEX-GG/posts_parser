import random
import json
import requests
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.utils import read_from_json_file, get_post_item, get_post_item_1, get_post_item_2, get_post_item_3, get_post_item_4

app = FastAPI()

app.mount("/photo", StaticFiles(directory="photo"), name="photo")

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
        1: 'zapchasti774.json',             # Зайцев = zapchasti774.ru    --- --- --- ---
        2: 'zapchasti174.json',             # Артёмова = zapchasti174.ru  +++ +++ +++ +++ +++ +++ +++ +++ +++ +++
        3: 'part-servis.json',              # --- --- --- --- --- --- --- --- --- --- ---
        4: 'instrument-oborudovanie.json',  # --- --- --- --- --- --- --- --- --- --- ---
        5: 'stroy-mechanizaciya.json',      # Почивалов = строй-механизация.рф + partmarket.online +++ +++ +++ +++
        6: 'stroi-materialy74.json',        # Жижелева = stroi-materialy74.ru +++ +++ +++ +++ +++ +++ +++ +++ +++
        7: 'stroimaterialy74.json',         #
        8: 'metallstanki74.json',           # ---
        9: 'metall-tech74.json',            # Дерюгин = metall-tech74.ru + metallpro.site +++ +++ +++ +++ +++ +++
        10: 'so-1.json',                    # Мишарин = so-1.ru + pro-zapchasti.online +++ +++ +++ +++ +++ +++ +++
        11: '1-stk.json',                   # Кудрявцева = 1-stk.ru + pro-stk.online +++ +++ +++ +++ +++ +++ +++ +++
        12: 'm-ob.json',                    # Пушкин = m-ob.ru + motor-tech.online + motortech.site
        13: 'smt174.json'                   # Ребрик = smt174.ru + best-part.site
    }
    result = read_from_json_file(file_name=page_filters[params.page])
    return {'posts': result}


@app.get("/post")
async def post():
    result = read_from_json_file(file_name='zapchasti774.json')
    return {'posts': result}

@app.get("/post_1")
async def post():
    result = read_from_json_file(file_name='spec-stroi174.json')
    return {'posts': result}

@app.get("/post_2")
async def post_2():
    result = read_from_json_file(file_name='1-stk.json')
    return {'posts': result}

@app.get("/post_3")
async def post_3():
    result = read_from_json_file(file_name='m-ob.json')
    return {'posts': result}

@app.get("/post_4")
async def post_4():
    result = read_from_json_file(file_name='shesterenka_4.json')
    return {'posts': result}


@app.get("/post/{item_id}")
async def post_item(item_id):
    result = get_post_item(item_id)
    return {"post_item": result}

@app.get("/post_1/{item_id}")
async def post_item_1(item_id):
    result = get_post_item_1(item_id)
    return {"post_item": result}

@app.get("/post_2/{item_id}")
async def post_item_2(item_id):
    result = get_post_item_2(item_id)
    return {"post_item": result}

@app.get("/post_3/{item_id}")
async def post_item_3(item_id):
    result = get_post_item_3(item_id)
    return {"post_item": result}

@app.get("/post_4/{item_id}")
async def post_item_4(item_id):
    result = get_post_item_4(item_id)
    return {"post_item": result}


@app.get("/payment/stroy_mech/generate")
async def get_stroy_mech_payment_ref(amount: int, email: str | None = None):
    response = await generate_stroy_mech_payment_ref(amount=amount, email=email)
    return response


async def generate_stroy_mech_payment_ref(amount: int, email: str | None = None):

    order_number = str(random.randint(10000000, 99999999))
    return_url = "https://partmarket.online/"

    if email:
        url = f"https://bankwallet.ru/payment/rest/register.do?amount={amount}&currency=643&orderNumber={order_number}&returnUrl={return_url}&userName=StroyMechanization-api&password=a6Zj8Ht9Nw!&email={email}"  # TEST URL
    else:
        url = f"https://bankwallet.ru/payment/rest/register.do?amount={amount}&currency=643&orderNumber={order_number}&returnUrl={return_url}&userName=StroyMechanization-api&password=a6Zj8Ht9Nw!"  # TEST URL

    response = requests.get(url)
    return response.json()

