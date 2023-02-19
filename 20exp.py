n=input("Enter the string")
a={}
for i in n:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
for m,n in a.items():
    print(m,n)

