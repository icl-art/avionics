@echo off
cd /d %~dp0
TITLE Getting Data

mpfshell -o COM7 -n -c "ls; get log.bin; exit"

move log.bin ../bin/log.bin

python data_read.py -d ../bin -i log.bin -o log.csv

ECHO Processing Data
copy /V /Y /Z log.csv ..\data_processing\astra.csv

cd ..\data_processing

matlab -r "astra"

PAUSE
