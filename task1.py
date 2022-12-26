def sum(spisok):
    sum = 0
    for i in range (1, len(spisok), 2):
        sum += spisok[i]
    return sum

list = [2, 3, 5, 9, 3]

result = sum(list)
print(list)
print(f'Cуммa элементов списка, стоящих на нечётной позиции. = {result}')