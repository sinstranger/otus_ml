"""
Написать программу, которая получает на вход строку и возвращает словарь, где:
ключи — символы из этой строки;
значения — количество раз, сколько каждый символ встречается.
"""

input_string = input("Input: ")
result = {}
for i in input_string:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for k, v in result.items():
    print(f"{k}: {v}")
