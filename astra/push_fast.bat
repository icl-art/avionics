@echo off
cd /d %~dp0
TITLE Pushing Code

ECHO Compiling libs

echo | call compile.bat

mpfshell -o COM5 -n -c "ls; put datacap.py main.py; mput.*\.mpy; ls; exit"

ECHO Done

PAUSE