import os
import datetime
import shutil
import time


import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
source = '/Users/Cody/Desktop/folder_A/'
destination = '/Users/Cody/Desktop/Folder_B/'

for root, dirs,files in os.walk(source):  
    for i in files:
        path = os.path.join(root, i)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True:  ", i, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.copy(path, destination)
           
