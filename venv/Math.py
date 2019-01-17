import math
for i in range(1,501):
    a=math.sqrt(i)
    print(a)


a=10
b =2
if a==b:
    print("your result will not crt")
if a!=b :
    print("your result will not crt")

x=3
if x==3:
    print("true")  #if condition is  true it will not check next conditions
elif x==1:
    print("false")
elif x==0:           #it will skip automatically.
    print("false")
else:
    print("result")

#while conditions

i=1
while (i<=4):
    print("hello")
    i=i+1
j=1
while (j<=4):
    print("world")
    j=j+1


print(i,j)