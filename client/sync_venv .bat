@echo off
if not exist ".\venv\Scripts\activate.bat" (
    echo creating venv...
    python -m venv venv
)
call .\venv\Scripts\activate.bat

echo.
echo updating pip...
python -m pip install --upgrade pip

echo.
echo synchronising packages with requirements.txt...
if exist ".\requirements.txt" (
    python -m pip install -r requirements.txt
)
python -m pip freeze > requirements.txt

echo.
echo packages has been synchronised with requirements.txt...
pause