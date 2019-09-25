from io import StringIO
import sys


class CsvReader:
    def __init__(self,file):
        self.file:StringIO=file

    def helper_file_offsets(self):
        res={}
        i=1
        self.file.seek(0)
        file_cursor = self.file
        line = file_cursor.readline()
        while line:
            res[i]=file_cursor.tell()
            line=file_cursor.readline()
            i+=1
        return res


    def print_file(self)->None:
        self.file.seek(0)
        line=self.file.readline()
        while line:
            print(line)
            line = self.file.readline()

    def get_line(self,line_numer:int):
        try:
            self.file.seek(0)
            headers = self.file.readline().replace('\n','').split(',')
            self.file.seek(self.helper_file_offsets()[line_numer])
            values = self.file.readline().replace('\n','').split(',')
            return dict(zip(headers,values))

        except IOError:
            print("Out of bound")
        except ValueError:
            print('Non-numeric data found in the file.')

        except OSError:
            print('Some OSError.')
        except:
            print("Error")

    def write_file(self,new_path):
        self.file.seek(0)
        file_cur=self.file
        with open(new_path,'w') as new_file_obj:
            for line in file_cur:
                new_file_obj.write(line)






def example():
    csv = """name,country,age
dror,portugal,32
mango,portugal,5
may,portugal,1
ido,portugal,1
nitzan,portugal,32
"""


    with StringIO(csv) as file_obj:
        c1 = CsvReader(file_obj)
        c1.print_file()
        print(c1.get_line(40))



def mainn():
    path = sys.argv[1]
    with open(path) as file_obj:
      c2=CsvReader(file_obj)
      print(c2.get_line(3))
      c2.print_file()

def test():
    path = sys.argv[1]
    with open(path) as file_obj:
        for line in file_obj:
            print(line)


def file_iterator(file):
    line=file.readline()
    while line:
        yield line
        line=file.readline()


class iterd():
    def __init__(self,capacity):
        self.capacity=capacity
        self.index=1

    def __iter__(self):
        return self

    def __next__(self):
        temp=self.index
        if temp<self.capacity:
            self.index+=1
            return temp
        else:
            raise StopIteration

def generator_seq(capacity):

    index=1
    while index<capacity:
        yield index
        index+=1


def main_iteration():
    x=generator_seq(10)
    line=next(x)

    while line:
        try:
            print(line)
            line=next(x)
        except StopIteration:
            break

def main_with_write():
    path = sys.argv[1]
    with open(path) as file_obj:
        c2=CsvReader(file_obj)
        c2.write_file("/Users/dsivan/GitRepos/PythonUtilities/Examples/readFile/output.csv")

# mainn()
# example()
# test()
# main_with_write()










