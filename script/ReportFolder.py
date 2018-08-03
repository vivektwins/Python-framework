from generic import *
from datetime import date
from datetime import datetime
import os,glob,shutil


#Getting the today's date and time

today = str(date.today())
print (today)
datetimeobject = datetime.strptime(today,'%Y-%m-%d')
new = datetimeobject.strftime('%m-%d-%Y')
print(new)

time = datetime.now()
print(time)

Html = []

#Making the directory in the name of today's folder

file_path = ".\\StumpNew"
    #directory = os.path.dirname(file_path)
try:
    print(os.getcwd())
    if not os.path.exists(file_path):
        os.chdir("C:\\Users\\Hasher\\PycharmProjects\\StumpNew")
        print("pass")
        os.mkdir(str(today))
        print(os.getcwd())
    else:
        print("path is already created")

except OSError:
    print('Error: Creating directory. ' + file_path)

#Finding the path and separating the file

folder_path = 'C://Users/Hasher/PycharmProjects/StumpNew/'
for filename in glob.glob(os.path.join(folder_path, '*.html')):
    with open(filename, 'r') as f:
        # print(filename)
        last = os.path.basename(filename)
        Html.append(last)
print(Html)

#Finding the creation time of the file and copying into the respective folder

modifieddate = []
for h in Html:
    created = os.stat(h).st_ctime
    data = date.fromtimestamp(created)
    if data.strftime('%Y-%m-%d') == today:
        shutil.copy2(h, today)

#     print(modifieddate)
#     print(Html)
# for m in modifieddate:
#         if today == m:
#             print(Html)
#




