#!/bin/bash

# Check if Python is already installed
if command -v python &> /dev/null; then
  echo "Python is already installed."
else
  echo "Installing Python"
fi

# Install pip
python3 -m ensurepip

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the packages specified in the requirements.txt file
pip3 install -r requirements.txt

# Trigger the app.py
python app.py --csv data.csv