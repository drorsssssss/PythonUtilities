


def fib():
    res=1
    last_res=1

    yield res
    yield res

    while True:
        tmp=res
        res +=last_res
        last_res=tmp

        yield res






x=fib()
cnt=0
for i in x:
    if cnt==6:
      print(i)
      break
    cnt+=1