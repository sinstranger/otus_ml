line = input("Input a line: ")
print(sum(int(i) for i in line if i.isnumeric()))
