Dictionary1 = { 'A': ['Geeks',56], 'B': [4,'Schwifty'], 'C': ['Geeks',56.0] }
  
print("Dictionary items:")
  
# Printing all the items of the Dictionary
print(Dictionary1.items())

for element in Dictionary1.items():
    print(element[0])