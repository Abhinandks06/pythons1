txt=input("Enter the text")
txt1=txt.split(" ")
print(txt1)
dict={}
for n in txt1:
    if n in dict:
        dict[n]=dict[n]+1
    else:
        dict[n]=1
for m,n in dict.items():
    print(m,n)