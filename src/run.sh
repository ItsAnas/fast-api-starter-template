#!/bin/sh

python3 -m venv env
. env/bin/activate
pip install -r requirements.txt

cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
