@echo off
TITLE Data Logger

:: get current WiFi network
for /f "tokens=2 delims=:" %%a in ('netsh wlan show interface name="WiFi" ^| find "Profile"') do set wn=%%a
:: remove preceding space
set wn=%wn:~1%

:: get local IP of computer
for /f "tokens=2 delims=:" %%b in ('ipconfig ^| find "IPv4"') do set ip=%%b
:: remove preceding space
set ip=%ip:~1%

:: checking arduino code
echo WiFi Network is %wn%
echo Local IP is %ip%
echo Check this is the same as the program flashed to the arduino
pause

:: switch to local dir
cd /D "%~dp0"

:: open web page
set page=http://%ip%:8080
start "" http://%ip%:8080

:: start client 
start "Client" /Min client.exe "%ip%"

