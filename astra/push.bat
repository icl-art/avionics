@echo off
cd /d %~dp0
TITLE Pushing Code

:start
set /p portsel="Enter COM Port: "
echo COM%portsel% selected 

set /p fname="Enter file to push, inc extension: "
echo Pushing %fname%
CHOICE /C YN /M "Continue "
IF %ERRORLEVEL% == 1 (GOTO push)
IF %ERRORLEVEL% == 2 (GOTO start)

:push
mpfshell -o COM%portsel% -n -c "ls; put %fname% main.py; mput.*\.mpy; ls; exit"
PAUSE
