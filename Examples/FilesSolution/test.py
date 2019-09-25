import os
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d')
    return formated_date

def test_func(*args,**kwargs):
    for k,v in kwargs.items():
        print(k,v)

    print(type(kwargs))
    for i in  args:
        print(i)
    print(type(args))

root_path="/Users/dsivan/GitRepos/PythonUtilities/Examples/FilesSolution"

# with os.scandir(root_path) as fileIterator:
#     for obj in fileIterator:
#         if obj.is_dir():
#             print(convert_date(obj.stat().st_mtime))

def ex1():
    for dirpath,dirnames,files in os.walk(root_path):
        print(dirpath)
        #print(dirnames)
        for file in files:
            print(file)

# ex1()

