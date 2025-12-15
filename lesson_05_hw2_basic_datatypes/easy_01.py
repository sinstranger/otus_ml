collector = []
while True:
    item = input("Input a number: ")
    if item.isnumeric():
        collector.append(int(item))
    else:
        break

print(sum(collector))
