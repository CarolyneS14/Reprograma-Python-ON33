# ## Atividade 4: Função de Contagem de Caracteres

# ### Descrição

# Crie uma função que conta o número de caracteres em uma string fornecida pelo usuário. Use `try` e `except` para garantir que a entrada seja uma string.

# ### Passos

# 1. Crie uma função `contar_caracteres` que recebe um parâmetro.
# 2. Use a função interna `len` para contar o número de caracteres na string e retorne o resultado.
# 3. Peça ao usuário para inserir uma string.
# 4. Use `try` e `except` para garantir que a entrada seja uma string.
# 5. Chame a função `contar_caracteres` e exiba o resultado.

# ---

def contarCaracteres(texto):
    return len(texto)

entrada = input('Digite uma palavra ou uma frase: ')

try:
    caracteres = contarCaracteres(entrada)
    print(f'A string {entrada}, tem {caracteres} caracteres')
except:
    print('Erro, digite uma palavra ou frase')
