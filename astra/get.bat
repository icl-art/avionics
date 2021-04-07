@echo off
cd /d %~dp0
TITLE Getting Data

:start
set /p portsel="Enter COM Port: "
echo COM%portsel% selected 

CHOICE /C YN /M "Continue "
IF %ERRORLEVEL% == 1 (GOTO push)
IF %ERRORLEVEL% == 2 (GOTO start)

:get
mpfshell -o COM%portsel% -n -c "get out.csv out.csv; exit"
PAUSE
