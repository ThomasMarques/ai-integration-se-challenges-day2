#!/bin/bash
PWD=$(pwd)
echo "Current working directory: $PWD"
ls -al
ls -al venv/bin/
export PATH="$PWD/venv/bin:$PATH"
source venv/bin/activate
ls -al $PWD/venv/bin/uvicorn
$PWD/venv/bin/uvicorn --workers 4 good_wine_api.main:app --host 0.0.0.0 --port 8000