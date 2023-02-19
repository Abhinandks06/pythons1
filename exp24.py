n=int(input("Enter the number of terms"))
print("Enter the elements")
a=[]
for i in range(0,n):
          list=int(input())
          if(list%2!=0):
              a.append(list)
print("The entered list without even numbers is ")
print(a)