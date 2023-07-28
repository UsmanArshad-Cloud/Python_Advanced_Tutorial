#Generators are type of iterable that are like list,tuple or set but the only difference is that
#they create the value on the fly rather than loading all in the memory

def fibonacci_no(n):
    x1 = 0
    x2 = 1
    for i in range(n):
        result = x1+x2
        temp=x1
        x1=x2
        x2=temp+x2
        yield result

result=fibonacci_no(100)
for r in result:
    print(r)
#or you can write print(next(fibonacci_no(100))) to ge 1 by 1