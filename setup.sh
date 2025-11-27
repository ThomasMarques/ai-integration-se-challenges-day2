#!/bin/bash
pip install -Ur requirements.txt
pip list
uvicorn --workers 4 good_wine_api.main:app --host 0.0.0.0 --port 8000