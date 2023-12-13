@echo off
call .\venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
call .\venv\Scripts\deactivate.bat
pause