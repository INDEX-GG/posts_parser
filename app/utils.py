import json
from string import digits
import random
import os


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
    with open(file_name, 'r') as f:
        for line in f:
            try:
                result.append(json.loads(line.replace("'", '"').replace('\\xa0', ' ')))
            except:
                pass
    return result
