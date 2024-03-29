#!/usr/bin/env bash

sudo python3 -m venv venv
source venv/bin/activate
pip install -U pip setuptools build
cp .env.example .env
cat ./app/db.sql | sqlite3 ./app/db.sqlite3