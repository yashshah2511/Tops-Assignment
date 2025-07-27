lst=[1,1,2,2,3,3,4,4,4,4,5,5,5]
dicti={}
count=1
for i in lst:
    if i in dicti:
        dicti[i]+=1
    else:
        dicti[i]=1
    
print(dicti)