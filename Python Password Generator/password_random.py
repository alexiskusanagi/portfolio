import sys
import random

print('Digite 1 para gerar Senha Aleatória de 8 caracteres \nou 0 para Sair')

comando = int(input())

if comando == 0:
    sys.exit()

elif comando == 1:
    
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%¨&*()_+^:><"

    senha = ""

    for char in range(8):
        senha += random.choice(caracteres)
    print(f'Senha Gerada: {senha}')

else :
    print('operação inválida. Fechando sistema')   
    sys.exit() 
