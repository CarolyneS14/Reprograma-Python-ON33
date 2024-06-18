# ## Atividade 2: Função de Verificação de Par ou Ímpar

# ### Descrição

# Crie uma função que verifica se um número é par ou ímpar. Use `try` e `except` para garantir que a entrada seja um número.

# ### Passos

# 1. Crie uma função `verificar_par_impar` que recebe um parâmetro.
# 2. Use uma condicional `if` para verificar se o número é par ou ímpar e retorne a string apropriada.
# 3. Peça ao usuário para inserir um número.
# 4. Use `try` e `except` para garantir que a entrada seja um número.
# 5. Chame a função `verificar_par_impar` e exiba o resultado.


def parImpar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'
    
entrada = input('Digite um numero inteiro: ')

try:
    numero = int(entrada)
    resultado = parImpar(numero)
    print(f'O numero {numero} e {resultado}')

except:
    print('Erro: Digite um numero inteiro')
