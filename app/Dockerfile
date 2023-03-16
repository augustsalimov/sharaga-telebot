FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt .
RUN  pip install -U pip && pip install -r requirements.txt --no-cache-dir

COPY . ./