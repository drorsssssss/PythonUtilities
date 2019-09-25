




def MaxOverlapInterval(arr):
    start=[]
    end=[]
    while len(arr) >0:
        pair = arr.pop()
        start.append(pair[0])
        end.append(pair[1])

    start.sort()
    end.sort()

    c=1
    global_count=0
    j=0
    i=0
    while i<=len(start)-1 and j<=len(end)-1:
        if start[i]<=end[j]:
            c+=1
            global_count=max(global_count,c)
        else:
            c-=1
            j+=1
        i+=1
    return global_count




input={(0,2),(3,7),(4,6),(7,8),(1,5)}

print(MaxOverlapInterval(input))