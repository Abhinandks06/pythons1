n=int(input("Enter the size"))
a=[]
print("Enter the elements of list")
for i in range(0,n):
    s=int(input())
    if(s>100):
        a.append("over")
    else:
        a.append(s)
print(a)
