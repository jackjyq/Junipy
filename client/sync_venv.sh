#!/bin/bash
if source "./venv/bin/activate";
then
    :
else
    echo "creating venv..."
    python3 -m venv venv &&
    source "./venv/bin/activate"
fi

echo
echo "updating pip..."
python3 -m pip install --upgrade pip

echo
echo "synchronising packages with requirements.txt..."
if [ ! -f ./requirements.txt ];
then
    :
else
    python3 -m pip install -r requirements.txt
fi
python3 -m pip freeze > requirements.txt

echo
echo "packages has been synchronised with requirements.txt..."
