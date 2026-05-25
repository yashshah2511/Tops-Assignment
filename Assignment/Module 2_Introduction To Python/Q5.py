a=input("enter the string")

if(len(a)<3):
    print("string is too short")
elif(a.endswith("ing")):
    print(a + "ly")
else:
    print(a + "ing")