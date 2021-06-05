@echo off
cd /d %~dp0
TITLE Pushing Code

ECHO Compiling libs

echo | call compile.bat

cd ../src

mpfshell -o COM3 -n -c "ls; put main.py main.py; mput.*\.mpy; ls; exit"

ECHO Done

PAUSE
