#!/bin/bash

# Install Homebrew (if not installed)
which -s brew
if [[ $? != 0 ]]; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
fi

# Check if Python is already installed
if command -v python &> /dev/null; then
  echo "Python is already installed."
else
  brew install python
fi

# Install MySQL
brew install mysql

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