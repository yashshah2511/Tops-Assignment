my_dict = {
    'apple': 50,
    'banana': 20,
    'cherry': 30,
    'date': 40
}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending Order by Value:")
print(asc_sorted)

# desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
# print("\nDescending Order by Value:")
# print(desc_sorted)

print(sorted(my_dict.values()))