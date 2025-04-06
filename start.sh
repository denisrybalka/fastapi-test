#!/bin/bash

# [fastapi] project start:
#  uvicorn main:app --reload
#  visit swagger:
#   http://127.0.0.1:8000/docs

# Define virtual environment name
VENV_NAME="fastapi_venv"

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_NAME/bin/activate

# Start FastAPI server
echo "Starting FastAPI..."
uvicorn main:app --reload
