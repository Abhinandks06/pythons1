n=int(input("enter the number of colours in list 1"))
a=[]
flag=0
print("Enter the colors")
for i in range(0,n):
    x=input()
    a.append(x)
m=int(input("Enter the number of colours in list 2"))
b=[]
c=[]
print("Enter the colors")
for i in range(0,m):
    y=input()
    b.append(y)
for i in a:
    for j in b:
        if(i==j):
            flag=flag+1
    if(flag==0):
        print(i)
    flag=0