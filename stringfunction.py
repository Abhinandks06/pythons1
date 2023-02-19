a=input("Enter the data")
x=a.isalpha()
if(x==True):
    print("The given data is an alphabet")
else:
    print("The given data is not an alphabet")
y=a.islower()
if (y == True):
   print("The given data is in lower case")
else:
   print("The given data is not in lower case")
z=a.isupper()
if (z == True):
   print("The given data is in upper case")
else:
   print("The given data is not in upper case")
b=a.isdigit()
if (b == True):
   print("The given data is a digit")
else:
   print("The given data is not a digit")
c=a.isalnum()
if (c == True):
   print("The given data contain alpha numerics ")
else:
   print("The given data is not alphanumeric")
d=a.isnumeric()
if (d == True):
   print("The given data is numeric")
else:
   print("The given data is not a numeric")
e=a.isspace()
if (e == True):
   print("The given data contains whitespaces only")
else:
   print("all the charectors are not whitespaces")
f=a.istitle()
if (f== True):
   print("The given data has a title ")
else:
   print("The given data does not contain a title")


