

with open("/Users/dsivan/GitRepos/PythonUtilities/Examples/AsyncIO/urls.txt",'r') as f:
    line=f.readline()
    while line:
        print(line)
        line=f.readline()
