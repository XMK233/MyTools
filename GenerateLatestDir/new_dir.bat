@echo off & python -x "%~f0" %* & goto :eof
import os, re
from datetime import datetime, timedelta
latest_folder = None
latest_date = None
for _ in os.listdir(os.getcwd()):
    folder = os.path.join(os.getcwd(), _)
    if not os.path.isdir(folder):
        continue
    match = re.match(r"(\d{4}-\d{1,2}-\d{1,2})", _)
    # l = len(date_all)
    # if l <= 0:
    # 	continue
    if not match:
    	continue
    latest_folder = folder
    latest_date = _

latest_time = datetime.strptime(latest_date, '%Y-%m-%d')
yes_time = latest_time + timedelta(days=7)
current_time = yes_time.strftime('%Y-%m-%d')
os.makedirs(os.path.join(os.getcwd(), current_time))