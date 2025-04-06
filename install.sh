#!/bin/bash

# [fastapi] project install:
#  python3.10 -m venv fastapi_venv # creates a virtual env
#  source fastapi_venv/bin/activate # toggle to virtual env
#  pip3.10 install -r requirements.txt

# Define virtual environment name
VENV_NAME="fastapi_venv"

# Check if virtual environment exists, if not, create it
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment..."
    python3.10 -m venv $VENV_NAME
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_NAME/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Setup complete! To start the project, run: ./start.sh"
