num = int(input('Введите число: '))
half = ''
 
while num > 0:
    half = str(num % 2) + half
    num = num // 2
 
print(half)