a=[]
n=int(input("enter the number"))
for i in range(0,n):
    a.append(int(input("enter the number")))
    
print(a)

# a.sort()
# print(a[1])

for i in range(0, len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            
print(a[1])