#!/bin/bash
if source "./venv/bin/activate";
then
    :
else
    echo "creating venv..."
    python -m venv venv &&
    source "./venv/bin/activate"
fi

echo
echo "updating pip..."
python -m pip install --upgrade pip

echo
echo "synchronising packages with requirements.txt..."
if [ ! -f ./requirements.txt ];
then
    :
else
    python -m pip install -r requirements.txt
fi
python -m pip freeze > requirements.txt

echo
echo "packages has been synchronised with requirements.txt..."