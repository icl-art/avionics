@echo off

:: get local IP of computer
for /f "tokens=2 delims=:" %%b in ('ipconfig ^| find "IPv4"') do set ip=%%b
:: remove preceding space
set ip=%ip:~1%

:loop

echo Posting fake data
curl -i -X POST -d "pressure=10.4&temperature=4.2" http:/%ip%:8080/get
pause

GOTO loop