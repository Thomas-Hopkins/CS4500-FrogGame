#!/bin/sh 

# Set the path to the python executable on the machine.
# If the file "PYTHON_PATH" exists use the path specified there
PYTHON_PATH=python3
if [ -f "./PYTHON_PATH" ]; then
    PYTHON_PATH=$(cat PYTHON_PATH)
fi

if [ -d "./.venv" ]; then
    # Activate the python virtual environment for this script instance
    echo "Activating Python virtual environment..."

    . ./.venv/bin/activate

    python -m pip install -r requirements-dev.txt

    echo ""
else
    # Create a python virtual environment if it does not exist yet
    echo "Creating Python virtual environment..."

    $PYTHON_PATH -m venv .venv
    . ./.venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements-dev.txt
    pre-commit install

    echo "Finished setting up Python virtual environment!"
    echo ""
fi

cont="y"
while true
do
    # Run source\main.py
    python -m source.main

    # Ask if we want to run again
    echo ""
    echo "Run again? (y/n): "
    read cont
    if [ "$cont" != "y" ]; 
        then break
    fi
    echo ""
done
