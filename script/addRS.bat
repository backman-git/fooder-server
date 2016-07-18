@echo off
cd .\fooder\main\imageProcessCore
make extractRS ID=%1


cd ..\RS
make add ID=%1 long=%2 lat=%3 g=%4 b=%5
