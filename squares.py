#Lists & List Comprehensions

squares = []
#We start with an empty list called squares.

for value in range(1,11):
 #   square = value ** 2 
 #   squares.append(square)
     squares.append(value ** 2)
print(squares)

#At 4, we tell Python to loop through each value from 1 to 10 using the range() function. Inside the loop, the current value is raised to the second power and assigned to the variable square.
#At 6, each new value of square is appended to the list squares. Finally, when the loop has finished running, the list of squares is printed on line 7.



#List Comprehensions

squares = [value ** 2 for value in range(1,11)]
print(squares)

# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.