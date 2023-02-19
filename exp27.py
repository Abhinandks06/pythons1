x=input("Enter the string")
if(x[-3:]=='ing'):
    x+='ly'
else:
    x+='ing'
print(x)
