@echo off
:: check if virtual environment folder exists
if not exist "\env" (
    echo Creating virtual environment...
    python -m venv env
) else (
    echo virtual environment is already exists.
)

:: Activate the virtual environment
call \env\Scripts\activate

:: check for the requirements file and install the dependencies
if exist requirements.txt (
    echo Installing dependencies...
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
) else (
    echo requirements.txt not found. Please add it and re-run the script
)

echo Setup completed. environment activated and dependencies installed
pause