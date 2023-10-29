#!/bin/bash

# Check if Python is installed

if ! [[ -x "$(command -v python3)" ]]
then
    echo "python3 is not installed. In order to run this application,
    you must have Python3. Please visit 'https://www.python.org/downloads/' "
    exit
fi

# Create virtual environment and install requirements

python3 -m venv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
python3 ./main.py
deactivate







