@echo off
cd .\fooder\main\imageProcessCore
make extractFD ID=$2

cd ..\FD
make add RSID=$1 ID=$2 g=$3 b=$4
