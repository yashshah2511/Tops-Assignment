# num=int(input("enter the number"))
# list1=[]
# unique=[]
# for i in range(0,num):
#     j=input("enter the number of the list")
#     list1.append(j)
    
# print(list1)

# unique_list = list(set(list1))
# print("Unique values from the list:", unique_list)



l = [10,20,5,4,8,24,5,7,5]
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)

print(l2)

