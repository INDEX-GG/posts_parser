FROM python:3.10.4
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ../products/zapchasti774.json /code/zapchasti774.json
COPY ../products/zapchasti174.json /code/zapchasti174.json
COPY ../products/part-servis.json /code/part-servis.json
COPY ../products/instrument-oborudovanie.json /code/instrument-oborudovanie.json
COPY ../products/stroy-mechanizaciya.json /code/stroy-mechanizaciya.json
COPY ../products/stroi-materialy74.json /code/stroi-materialy74.json
COPY ../products/stroimaterialy74.json /code/stroimaterialy74.json
COPY ../products/m-ob.json /code/m-ob.json
COPY ../products/metall-tech74.json /code/metall-tech74.json

COPY ../products/metallstanki74.json /code/metallstanki74.json
COPY ../products/smt174.json /code/smt174.json
COPY ../products/so-1.json /code/so-1.json
COPY ../products/1-stk.json /code/1-stk.json

COPY ../photo /code/photo
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
