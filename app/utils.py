import random
import os
import json
import requests
from string import digits


def generate_vendor_code() -> str:
    return ''.join(random.choice(digits) for _ in range(12))


def write_to_file(posts: list, file_name: str) -> None:
    if not os.path.isfile(file_name):
        open(file_name, 'a').close()
    with open(file_name, 'w') as f:
        for post in posts:
            f.write(str(post) + '\n')


def read_from_file(file_name: str) -> list:
    result = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                result.append(json.loads(line.replace("'", '"').replace('\\xa0', ' ')))
            except:
                pass
    return result


def read_from_json_file(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as read_file:
        result = json.load(read_file)
    return result


def get_post_item(item_id: int) -> list:
    sub_string = str(item_id)
    with open('zapchasti774.json', 'r', encoding='utf-8') as read_file:
        input_dict = json.load(read_file)
        for i in range(len(input_dict)):
            if input_dict[i]['id'] == sub_string:
                return input_dict[i]


def str_to_int(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as read_file:
        input_dict = json.load(read_file)
        for i in range(len(input_dict)):
            input_dict[i]['price'] = input_dict[i]['price'].replace(" ", "")
        output_dict = [x for x in input_dict if int(x['price']) >= 10000]
        qwe = json.dumps(output_dict, ensure_ascii=False)
    return input_dict


def upload_images(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as read_file:
        input_dict = json.load(read_file)
        for i in range(len(input_dict)):
            url = input_dict[i]['image']
            r = requests.get(url, allow_redirects=True)
            destination = str(i) + '.' + url.split('.')[-1]
            input_dict[i]['image'] = 'photo/stroimaterialy74/' + destination
            open(destination, 'wb').write(r.content)
        qwe = json.dumps(input_dict, ensure_ascii=False)
        print(qwe)
        return input_dict


def new_image(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as read_file:
        input_dict = json.load(read_file)
        for i in range(len(input_dict)):
            input_dict[i]['id'] = str(i)
        qwe = json.dumps(input_dict, ensure_ascii=False)
        print(qwe)
        return input_dict
