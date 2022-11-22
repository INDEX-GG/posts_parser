FROM python:3.10.4
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./one.json /code/one.json
COPY ./two.json /code/two.json
COPY ./three.json /code/three.json
COPY ./tor.json /code/tor.json
COPY ./zoom.json /code/zoom.json
COPY ./stroika.json /code/stroika.json
COPY ./stroika2.json /code/stroika2.json
COPY ./parser.json /code/parser.json
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]