@echo off
cd /d %~dp0
TITLE Getting Data

:start
set /p portsel="Enter COM Port: "
echo COM%portsel% selected 

CHOICE /C YN /M "Continue "
IF %ERRORLEVEL% == 1 (GOTO get)
IF %ERRORLEVEL% == 2 (GOTO start)

:get
mpfshell -o COM%portsel% -n -c "ls; get log.bin; exit"

set /p ofname="Enter output filename: "
python data_read.py -d "%cd%" -i log.bin -o %ofname% 
PAUSE
