#!/usr/bin/env bash

export FLASK_APP=./fix-server-side/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0