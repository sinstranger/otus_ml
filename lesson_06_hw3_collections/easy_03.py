"""
Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.
"""

inputs = [
    [1, 2, 3, 2, 4, 1, 5],
    ["a", "b", "a", "c", "b", "d"],
    [5, 5, 5, 5, 5],
    [1, 2, 3, 4, 5],
    [True, False, True, True, False],
    ["плюш", "шмяк", "бульк", "плюш", "шмяк", "хрясь"],
]

for input_line in inputs:
    seen = set()
    result_line = []
    for item in input_line:
        if item not in seen:
            result_line.append(item)
            seen.add(item)
    print(f"source: {input_line}\nresult: {result_line}\n")
