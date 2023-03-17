FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install
RUN apt-get install -y sqlite3 libsqlite3-dev

RUN mkdir -p /code
WORKDIR /code

COPY requirements.txt .
RUN  pip install -U pip setuptools && pip install -r requirements.txt --no-cache-dir

COPY . .