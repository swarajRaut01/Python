num1=int(input("enter lower number"))
num2=int(input("enter hightr number"))

for i in range(num1,num2):
    if(i%7==0 and i%5==0):
        print(i)
        
