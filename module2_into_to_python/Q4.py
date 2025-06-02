a=input("enter the first string")
b=input("enter the second string")

if(len(a)<=2 or len(b)<=2):
    print("string has only 2 or less than 2 characters")
    
newa=b[:2]+a[2:]
newb=a[:2]+b[2:]

print(newa,newb)