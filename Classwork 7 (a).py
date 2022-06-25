a = int(input("Enter any number : "))

if(a<0):
    print("Negative")

elif(a>0):
    print("Positive")

elif(a==0):
    print("Zero") 

a = int(input("Enter any number : "))

if(a<10):
    print("one digit")
elif(a<100) :
    print("two digit")
elif(a<1000):
    print("three digit")
elif(a>1000):
    print("more than three digit")

a = int(input("Enter any number : "))
b = int(input("Enter any number : "))
c = int(input("Enter any number : "))

if(a<b and a<c):
    print(a)
elif(b<a and b<c):
    print(b)
else:
    print(c) 

a = str(input("Enter any number : "))

if(a>="A" and a<="Z") :
    print("uppercase")

elif(a>="a" and a<="z") :
    print("lowercase")

else :
    print("number") 
