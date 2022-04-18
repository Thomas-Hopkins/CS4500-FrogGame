@echo off

rem Set the path to the python executable on the machine.
rem If the file "PYTHON_PATH" exists use the path specified there.
if exist ".\PYTHON_PATH" (
    set /P PYTHON_PATH=<PYTHON_PATH
) else (
    set PYTHON_PATH=python
)

if exist ".\.venv" (
    rem Activate the python virtual environment for this script instance
    echo Activating Python virtual environment...

    call .\.venv\Scripts\activate.bat

    echo(
) else (
    rem Create a python virtual environment if it does not exist yet
    echo Creating Python virtual environment...

    %PYTHON_PATH% -m venv .venv
    call .\.venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    pre-commit install

    echo Finished setting up Python virtual environment!
    echo(
)

cd source
:main
set cont="y"
rem Run source\main.py
python -m main
echo(

rem Ask if we want to run again
set /p cont=Run again? (y/n): %=%
If %cont%==y (
    echo(
    goto main
)
