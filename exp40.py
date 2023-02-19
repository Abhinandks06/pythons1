f1=open("demo.txt","r")
f2=open("odd.txt", "w")
content=f1.readlines()
for i in range(0,len(content)):
    if(i%2!=0):
        f2.write(content[i])
    else:
        pass
f2.close
f1.close
f2=open("odd.txt", "r")
p=f2.read()
print("Odd lines \n",p)
f2.close
