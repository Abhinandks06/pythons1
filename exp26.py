x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
if(x>y):
    temp=y
else:
    temp=x
for i in range(1,temp+1):
    if((x%i==0)and(y%i==0)):
         gcd=i
print("GCD of the given numbers are",gcd)