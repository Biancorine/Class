import os
import time
import sys

sexo = ''
msg = ''

os.system('clear')
sexo = input('digite o sexo M/F ')

if sexo == 'F':
    msg = 'Trata-se de uma Mulher'
else:
    msg = 'Trata-se de um Homem'

os.system('clear')

print(msg)

time.sleep(5)
sys.exit