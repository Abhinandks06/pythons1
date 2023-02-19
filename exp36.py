class rectangle:
    def __init__(self,l,b):
        self.__l=l
        self.__b=b
    def __gt__(self, other):
        if ((self.__l*self.__b)>(other.__l*other.__b)):
            return True
        else:
            return False
print("First rectangle")
l1=int(input("Enter the lenght of the rectangele"))
b1=int(input("Enter the breadth of the rectangele"))
a=rectangle(l1,b1)
print("Second rectangle")
l2=int(input("Enter the lenght of the rectangele"))
b2=int(input("Enter the breadth of the rectangele"))
b=rectangle(l2,b2)
if(a>b):
    print("First rectangle has more area")
else:
    print("Second rectangle has more area")