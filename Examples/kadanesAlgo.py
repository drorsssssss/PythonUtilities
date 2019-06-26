''' Kadanes Algo '''

def maxSunSeq(arr):
    max_local=0
    max_global=arr[-1]
    i=len(arr)-1

    while i>=0:
        max_local=max(arr[i],max_local+arr[i])
        if max_local>max_global:
            max_global=max_local
        i-=1

    return max_global


arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSunSeq(arr))



