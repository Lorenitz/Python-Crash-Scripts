#TUPLE - Sometimes you will want to create a list of items that cannot change. Tuples allow you to do that. Python refers to values that cannot change as immutable, 
#and an immutable list is called a tuple.

dimensions = (200,50)

#print(dimensions[0])
#print(dimensions[1])

#for dimension in dimensions:
#    print(dimension)


print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)    