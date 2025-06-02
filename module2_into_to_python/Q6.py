a=input("enter the string which having not poor words ") # "This movie is not that poor!"


s=a.find("not")
y=a.find("poor")
print(s,y)
if(s!=-1 and y!=-1):
    if(s<=y):
        print(a[:s]+'good'+a[y+4:])
    else:
        print(a)
else:
    print(a)