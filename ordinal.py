list1=["APPLE","ORANGE"]
print(list1)
list2=[]
for i in list1:
    for j in i:
        res=ord(j)
        list2.append(res)
print(list2)