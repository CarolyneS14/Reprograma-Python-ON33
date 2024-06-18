# Crie uma função que soma dois números fornecidos pelo usuário.
# Use try e except para garantir que as entradas sejam números e exiba o resultado da soma.
# Utilize if e else para verificar se a soma é positiva, negativa ou zero.

def somar_numeros():
    try:
        # Solicita ao usuário que insira dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Soma os números
        soma = num1 + num2
        
        # Verifica se a soma é positiva, negativa ou zero e exibe o resultado
        if soma > 0:
            print(f"A soma é positiva: {soma}")
        elif soma < 0:
            print(f"A soma é negativa: {soma}")
        else:
            print("A soma é zero.")
    except ValueError:
        print("Por favor, insira apenas números.")

# Chama a função
somar_numeros()
