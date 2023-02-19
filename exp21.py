string=input("Enter the string")
a={}
print(string)
for i in string:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
for m,n in a.items():
    print(m,n)


