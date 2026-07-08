a=input("enter the sentence")
b=[]
x={}
# print(type(x))
print(a)

b=a.split()

print(b)

for i in b:
    if(i in x):
        x[i]+=1
    else:
        x[i]=1
print(x)
