a = int(input("Enter any number : "))

for i in range(1,a+1):
    print(a+i)
    

a = int(input("Enter any number : "))


f=1

for i in range(1,a+1):
    f=f*1

print(f)


a = int(input("Enter a number : "))


b = [2,4,6,8,10]

for i in range(1,11):
    print(a*i)


a = int(input("Enter a number : "))

for i in range(1,a):
    if(i%2==0):
        print(i)

a = int(input("Enter a number : "))

c =True

for i in range(2,a):
    if(a%i!=0):
        c = False

if(c==True):
        print("prime")
else:
    print("not prime")

c = int(input("Enter : "))
a = str(c)
b = " "
for i in range(3,-1,-1):
    z = a[i]
    b = b + z
print(b) 

  
