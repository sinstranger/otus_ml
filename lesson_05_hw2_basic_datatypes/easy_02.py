line_with_different_cases = input("Input a line of text: ")
result = ""
for i in line_with_different_cases:
    if i.isupper():
        result += i

print(result)
