"""
Дана строка текста (или введённая через консоль).
Программа должна вернуть новую строку, в которой порядок слов будет обратным.
Пример:
"Python is really cool" → "cool really is Python".
"""

source = "Python is really cool" 
result = " ".join(source.split()[::-1])

print(result)
