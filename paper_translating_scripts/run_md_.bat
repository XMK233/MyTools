::cd Dropbox
start "C:\Program Files\Microsoft VS Code\Code.exe" source.pts
start "C:\Program Files\Microsoft VS Code\Code.exe" target.pts
call activate py1
python md.py
pause