<<<<<<< HEAD
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')


# Creat a square

import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Close the turtle graphics window on click
turtle.done()

=======
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')
>>>>>>> 538f33e54bd5be972e2358abb7e00b5e2e7d9865
