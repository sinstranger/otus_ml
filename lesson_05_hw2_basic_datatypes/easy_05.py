print("Input 10 numbers")
numbers = []
for i in range(10):
    number = int(input(f"Number {i + 1}: "))
    numbers.append(number)

print(f"Max number is {max(numbers)}")
