import math

p = q = e = d = int
ok_prime = True

def check_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    if num % 5 == 0:
        return False
    else:
        for c in range(2, num):
            if num % c == 0:
                return False
            else:
                return True



while ok_prime:
    p = int(input('Digite o valor primo p: '))
    if check_prime(p):
        print(f'{p} é primo. Entrada válida!')
        ok_prime = False
    else:
        print(f'{p} não é primo. Digite um número primo.')
ok_prime = True
while ok_prime:
    q = int(input('Digite o valor primo q: '))
    if check_prime(q):
        print(f'{q} é primo. Entrada válida.')
        ok_prime = False
    else:
        print(f'{q} não é primo. Digite um número primo.')
ok_prime = True
while ok_prime:
    e = int(input('Digite sua chave pública e: '))
    if check_prime(e):
        print(f'Sua chave pública {e} é um primo. Entrada válida.')
        ok_prime = False
    else:
        print(f'{e} não é primo. Digite uma chave pública válida.')







#if check_prime(7):
#    print('É primo')
#else:
#   print('Não é primo')