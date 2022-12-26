def numbers(spisok):
    list1 = []
    count = -1
    i = 0
    lenf = len(spisok) / 2
    while i < lenf:
        list1.append(spisok[i]*spisok[count])
        count -= 1
        i += 1
    return list1


spisok = [2, 3,5, 6]
spisokTwo = numbers(spisok)
print(spisok)
print(spisokTwo)