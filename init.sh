#!/usr/bin/env bash

sudo python3 -m venv venv
source venv/bin/activate
pip install -U pip setuptools build
pip install poetry
cp .env.example .env
poetry install