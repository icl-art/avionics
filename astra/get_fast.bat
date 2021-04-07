@echo off
cd /d %~dp0
TITLE Getting Data

:get
mpfshell -o COM5 -n -c "ls; get out.csv; exit"
PAUSE
