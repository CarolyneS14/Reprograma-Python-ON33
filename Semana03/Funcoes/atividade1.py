# ## Atividade 1: Função de Soma

# ### Descrição

# Crie uma função que soma dois números fornecidos pelo usuário. Use `try` e `except` para garantir que as entradas sejam números e exiba o resultado da soma.

# ### Passos

# 1. Crie uma função `soma` que recebe dois parâmetros.
# 2. Dentro da função, some os dois parâmetros e retorne o resultado.
# 3. Peça ao usuário para inserir dois números.
# 4. Use `try` e `except` para garantir que as entradas sejam números.
# 5. Chame a função `soma` e exiba o resultado.



def soma (a, b):
    return a + b

entrada1 = input("Insira o primeiro número: ")
entrada2 = input("Insira o segundo número: ")

try:
    numero1 = float(entrada1)
    numero2 = float(entrada2)
    resultado = soma(numero1, numero2)
    print(f"A soma de {numero1} e {numero2} e {resultado}")

except:
    print("Entrada invalida")    
