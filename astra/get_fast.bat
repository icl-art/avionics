@echo off
cd /d %~dp0
TITLE Getting Data

mpfshell -o COM5 -n -c "ls; get log.bin; exit"

ECHO %cd%
python data_read.py -d "%cd%" -i log.bin -o log.csv
PAUSE
