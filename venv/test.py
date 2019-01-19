a,b,c=1,2,1
print(a,b,c)

if a!=c:
    print("bool")

mystr = ["banana","roy"]
myit = iter(mystr)
print(next(myit))
print(next(myit))


x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
print("your code will be disabled")