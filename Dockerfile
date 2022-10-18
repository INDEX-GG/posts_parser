FROM python:3.10.4
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./yandex.txt /code/yandex.txt
COPY ./yandex2.txt /code/yandex2.txt
COPY ./yandex3.txt /code/yandex3.txt
COPY ./yandex6.txt /code/yandex6.txt
COPY ./yandex7.txt /code/yandex7.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]