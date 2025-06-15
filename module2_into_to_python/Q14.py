# Sample dictionary
my_dict = {
    'apple': 50,
    'banana': 20,
    'cherry': 30,
    'date': 40,
    'elderberry': 60,
    'fig': 10
}

# Find the top 3 highest values
top_3 = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3]

# Convert result to dictionary (optional)
top_3_dict = dict(top_3)

print("Top 3 highest values in the dictionary:")
print(top_3_dict)
