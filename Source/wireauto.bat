@echo off
:: disables echo feeback

set /p interface=Enter Interface (eg. Wi-Fi): 
set /p filter=Filter (eg. udp): 
:: gets interface and filter info from user

if "%interface%"=="" (
    set interface="Wi-Fi"
)
:: sets default interface

set file_dir=%cd%
:: gets script directory

break>"ipcache.txt"
:: resets IP cache file

set /p exclusion_list=Enter IP Exclusion List (y/n): 

if "%exclusion_list%"=="y" (
    notepad %file_dir%\ipcache.txt
)
:: opens IP exclusion file

if "%exclusion_list%"=="Y" (
    notepad %file_dir%\ipcache.txt
)
:: opens IP exclusion file

:main_loop

    cd C:\Program Files\Wireshark
    :: moves to wireshark directory

    if "%filter%"=="" (
        tshark -i "%interface%" -c 1 > "%file_dir%\data.txt"
    ) else (
        tshark -i "%interface%" -f "%filter%" -c 1 > "%file_dir%\data.txt"
    )
    :: runs wireshark scan

    cd "%file_dir%"
    :: changes back to original directory

    ip-check.py
    :: runs python script to anayalze IP data

goto main_loop