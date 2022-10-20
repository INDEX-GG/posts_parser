FROM python:3.10.4
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./yandex.txt /code/yandex.txt
COPY ./yandex2.txt /code/yandex2.txt
COPY ./yandex3.txt /code/yandex3.txt
COPY ./tor.json /code/tor.json
COPY ./zoom.json /code/zoom.json
COPY ./stroika.json /code/stroika.json
COPY ./stroika2.json /code/stroika2.json
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]