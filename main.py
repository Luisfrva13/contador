import os
import time

# USUÁRIO INFORMA NÚMERO
contador = int(input('Informe um número inteiro:'))
os.system('cls')

# CONTAR DO VALOR INFORMADO ATÉ 0
while contador >= 0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1

print('BOOOM!!!')



