a = int(input("Enter any number : "))
b = int(input("Enter any number : "))
c = int(input("Enter any number : "))

if(a>b and a>c):
   print (a)

elif(b>c and b>a) :
    print (b)

else:
    print (c) 


a = int(input("Enter any age : "))

if(a>1)and (a<10):
    print("Childeren")

elif(a>11)and(a<18) :
    print("Teenager")

elif(a>18 and a<60):
    print ("Adult")

elif ( a>60):
    print ("Senior")

a = int(input("Enter any Number : "))

b = a*1.8+32

print(b) 
