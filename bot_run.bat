@echo off
call %~dp0Pizza_Shop1\venv\Scripts\activate

cd %~dp0Pizza_Shop1

set TOKEN=5742744035:AAHYeK8hhKQ9cd3uY1zQ2mlz8NlzQbe6TpQ

python bot_telegram.py

pause