
def generate_even():
    i=0
    while True:
        yield i
        i+=2

for i in generate_even():
    if i>10:
        break
    print(i)