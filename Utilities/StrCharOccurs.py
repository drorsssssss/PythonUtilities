

def strCharOccurs(sstr,cchar):
    num=0
    for c in sstr:
        if c==cchar:
            num+=1


    return num



def noneReplce(lst):

    if lst is None:
        return None
    elif lst == []:
        return []
    else:
        last_val=lst[0]
        for idx, num in enumerate(lst):
            if num is None:
                lst[idx]=last_val
            else:
                last_val=num

        return lst


#print(strCharOccurs('drors ro','r'))

# input [1,2,None,3,None,None,4,5]

print(noneReplce(None))
