a=int(input("enter the first element of gcd"))
b=int(input("enter the second element of gcd"))

if(a<=b):
    temp=a
    a=b
    b=temp
r=a%b
    
while(r!=0):
    a=b
    b=r
    r=a%b
    
print("your gcd is",b)