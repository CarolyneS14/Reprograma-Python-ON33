try:
    numero1 = 10
    numero2 = 2
    resultado = numero1 / numero2
    print(f'O resultado e {resultado}')
except ZeroDivisionError:
    print('Segundo numero nao pode ser zero')
else:
    print('Divisao realizada com sucesso!')
finally:
    print('Fim da divisao')
