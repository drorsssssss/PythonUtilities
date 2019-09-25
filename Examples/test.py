def URLify(input):
    input,limit = input.split(",")
    i=0
    ls=[]
    while i<int(limit):
        if input[i]==' ':
            ls.append("%20")
        else:
            ls.append(input[i])
        i+=1
    return ''.join(ls)

print(URLify("mr john smith    ,13"))