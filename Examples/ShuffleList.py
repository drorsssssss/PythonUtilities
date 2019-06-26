import random

arr=[1,2,3,4,5]
res_arr=arr.copy()

for i in range(len(res_arr)-1,0,-1):
    j=random.randint(0,i+1)
    res_arr[i],res_arr[j] = res_arr[j],res_arr[i]

print(f"Original: {arr}")
print(f"Original: {res_arr}")