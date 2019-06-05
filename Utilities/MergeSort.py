
''' MergeSort '''

def _merge(lst,temp_lst,start,middle,end):
    left_idx=start
    right_idx=middle+1
    current=left_idx

    for i in range(len(lst)):
        temp_lst[i]=lst[i]

    while left_idx<=middle and right_idx<=end:
        if temp_lst[left_idx]<=temp_lst[right_idx]:
            lst[current]=temp_lst[left_idx]
            left_idx+=1
        else:
            lst[current]=temp_lst[right_idx]
            right_idx+=1

        current+=1

    remaining=middle-left_idx
    for i in range(remaining+1):
        lst[current+i]=temp_lst[left_idx+i]

def _mergeSort(lst,temp_lst,start,middle,end):
    if start<end:
        _mergeSort(lst,temp_lst,start,int(abs(middle-start)/2)+start,middle)
        #print(f"Left: {start,int(abs(middle-start)/2)+start,middle}")
        _mergeSort(lst,temp_lst,middle+1,int(abs(end-middle-1)/2)+middle+1,end)
        #print(f"Right: {middle+1,int(abs(end-middle-1)/2)+middle+1,end}")
        _merge(lst,temp_lst,start,middle,end)

def mergeSort(lst):
    temp_lst=[None]*len(lst)
    _mergeSort(lst,temp_lst,0,int((len(lst)-1)/2),len(lst)-1)


z=[5,6,7,3,2]
mergeSort(z)
print(z)
    