@echo off
REM --------------------------------------------------------
REM \Documents\GitHub\nbk5876.github.io\scanpc.bat
REM --------------------------------------------------------

echo Gathering system information...

echo OS Version: > SystemInfo.txt
wmic os get Caption, Version | more >> SystemInfo.txt

echo. >> SystemInfo.txt
echo Disk Usage:  >> SystemInfo.txt
wmic logicaldisk get caption, freespace, size | more  >> SystemInfo.txt

echo. >> SystemInfo.txt
echo Memory Usage: >> SystemInfo.txt
wmic os get FreePhysicalMemory,TotalVisibleMemorySize | more  >> SystemInfo.txt

echo. >> SystemInfo.txt
echo Running Processes: >> SystemInfo.txt
tasklist >> SystemInfo.txt

echo.
echo System information has been saved to SystemInfo.txt
echo Press any key to exit...
pause > nul
