n=int(input("entyer the number"))
list1=[]
list2=[]
z=0
y=0

def fact(j):
    if j==0:
        return 1
    else:
        return j*fact(j-1)

for i in range(1, n+1):
    if(i%2==0):
        list1.append(i)
    else:
        list2.append(i)
        
print(list1)
print(list2)

for j in list2:
    z=z+(j**2)/(fact(j))
    
print("odd series",z)


for k in list1:
    y=y+(k**2)/(fact(k))
    
print("even series",y)
# def fact(j):
#     if j == 0:
#         return 1
#     else:
#         return j * fact(j - 1)

# def odd_series_custom(n):
#     num = 12
#     total = 0
#     for i in range(1, n+1, 2):  # loop through odd numbers up to n
#         total += num / fact(i)
#         num += 20
#     return total

# # Input
# n = int(input("Enter the maximum odd number (n): "))
# result = odd_series_custom(n)
# print("Sum of the custom odd series is:", result)
