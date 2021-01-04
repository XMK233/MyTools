@echo off & python -x "%~f0" %* & goto :eof
import os

currentFolder = os.getcwd()

with open("convert_danmu.bat", "w") as cdb:
    cdb.write("call activate py1\n")
    for f in os.listdir(currentFolder):
        if ".xml" not in f:
            continue
        cdb.write('python main.pyw "{}" -o "{}"\n'.format(f, f.replace("xml", "ass")))