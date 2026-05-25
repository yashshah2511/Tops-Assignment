lst=[1,7,1,2,1,2,1,2,3,3,5,4,5,6,9]
lst2=[]

for i in lst:
    if i in lst2:
        pass
    else:
        lst2.append(i)
        
print(lst2)