from collections import defaultdict

def removeDupsNaive(lst):
    temp=set(lst)
    return list(temp)



def removeDups(lst):
    result=defaultdict(lambda:0)
    for i in lst:
        result[i]
    return list(result)


example=[1,2,3,3,'A','A']
#print(removeDupsNaive(example))
print(removeDups(example))