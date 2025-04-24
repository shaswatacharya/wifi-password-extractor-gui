@echo off
@REM IT changes the directory to same as .bat file 
set SCRIPT_DIR=%~dp0
@REM loads on same directory so no to directory conflicts
start pythonw.exe "%SCRIPT_DIR%main.py"


