@echo off

:: Install Chocolatey (if not installed)
IF NOT EXIST "%SYSTEMDRIVE%\ProgramData\chocolatey" (
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
)

:: Install MySQL
choco install mysql

:: Install Python 3
choco install python

:: Install pip
python3 -m ensurepip

:: Create a virtual environment
python3 -m venv venv

:: Activate the virtual environment
.\myenv\Scripts\activate

:: Install the packages specified in the requirements.txt file
pip3 install -r requirements.txt

:: Trigger the app.py
python app.py --csv data.csv