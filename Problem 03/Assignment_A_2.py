import os
import time
import sys

media = 0
n1 = 0
n2 = 0
status = ''

n1 = float(input('Digite a nota 1'))
n2 = float(input('Digite a nota 2'))
media = (n1 + n2) / 2

if media < 3:
    status = 'aluno reprovado'
elif media < 5:
    status = 'aluno de recuperação'
elif media < 6:
    status = 'aluno de exame'
else:
    status = 'aluno aprovado'

os.system('clear')
print(fA média do aluno é:{media:.2f}')
print(status)

time.sleep(5)
sys.exit