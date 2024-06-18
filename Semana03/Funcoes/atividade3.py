# ## Atividade 3: Função de Conversão de Temperatura

# ### Descrição

# Crie uma função que converte uma temperatura de graus Celsius para Fahrenheit. Use `try` e `except` para garantir que a entrada seja um número.

# ### Passos

# 1. Crie uma função `celsius_para_fahrenheit` que recebe um parâmetro.
# 2. Converta a temperatura de Celsius para Fahrenheit usando a fórmula: \( F = C \times \frac{9}{5} + 32 \).
# 3. Retorne a temperatura convertida.
# 4. Peça ao usuário para inserir uma temperatura em graus Celsius.
# 5. Use `try` e `except` para garantir que a entrada seja um número.
# 6. Chame a função `celsius_para_fahrenheit` e exiba o resultado.


def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

entrada = input('Digite a temperatura em graus Calsius: ')

try:
    celsius = float(entrada)
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"A temperatura de {celsius}C corresponde a {fahrenheit}F")
except:
    print("Erro, digite um numero valido")
