file_path="/Users/dsivan/GitRepos/PythonUtilities/Examples/FilesSolution/test.csv"

def iterate_file(file_path):
    with open(file_path) as file_obj:
        line=file_obj.readline()
        yield line.replace('\n','').split(',')
        line=file_obj.readline()
        while line:
            yield line.replace('\n','').split(',')
            line=file_obj.readline()

generator = iterate_file(file_path)
columns = next(generator)
for k in generator:
    print(dict(zip(columns,k)))

