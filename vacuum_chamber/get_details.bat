@echo off

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

pause