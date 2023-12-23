FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /app

RUN pip install --upgrade pip

COPY ./shop/requirements.txt requirements.txt

RUN pip install -r requirements.txt

#COPY docker-build/prestart.sh ./prestart.sh
COPY ./shop/ ./
