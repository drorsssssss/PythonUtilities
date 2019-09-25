def get_line(file,line_number):
    f = open(file,'r')
    headers=f.readline().replace('\n','').split(',')
    res = get_lines_lens(file)[line_number]
    f.seek(res)
    values = f.readline().replace('\n','').split(',')
    f.close()

    return dict(zip(headers,values))

def get_lines_lens(file):
    res={}
    f=open(file,'r')
    line=f.readline()
    i=1
    while line:
        res[i]=f.tell()
        i+=1
        line=f.readline()
    f.close()
    return res



print(get_line("/Users/dsivan/GitRepos/PythonUtilities/Examples/readFile/test.csv",3))

# print(get_lines_lens("/Users/dsivan/GitRepos/PythonUtilities/Examples/readFile/test.csv"))
