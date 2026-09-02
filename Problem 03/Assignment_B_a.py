

number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

if number1 > number2:
    diference = number1 - number2
elif number2 > number1:
    diference = number2 - number1
else:
    diference = 0

print(diference)