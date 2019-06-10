from collections import defaultdict
from array import array

def getDups(lst):
    result=defaultdict(lambda:0)
    for i in lst:
        result[i]+=1
    return result


def isHasDup(lst):
    result=defaultdict(lambda:0)
    for i in lst:
        result[i]+=1
        if result[i]>1:
            return True
    return False


#example = [1,2,3,4,5,6,7,8,'A','A']
arr=array(1,2,3,4)
#print(getDups(example))
print(isHasDup(example))



