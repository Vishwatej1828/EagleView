@echo off
:: check if virtual environment folder exists
if not exist "img_processing_env\" (
    echo Creating virtual environment...
    python -m venv img_processing_env
) else (
    echo virtual environment is already exists.
)

:: Activate the virtual environment
call img_processing_env\Scripts\activate

:: check for the requirements file and install dependencies
if exist requirements.txt (
    echo Installing dependencies...
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
) else (
    echo requirements.txt not found. Please add it and re-run the script
)

echo Setup completed. Virtual environment activated and dependencies installed
pause