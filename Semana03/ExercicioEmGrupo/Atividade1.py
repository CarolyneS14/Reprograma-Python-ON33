#Crie um programa onde a usuária deve inserir uma nota de 1 a 10 e o programa imprime se a aluna foi aprovada ou reprovada. 
# A nota mínima para aprovação é 7.

# Solicita à usuária que insira uma nota
nota = int(input("Informe sua nota de 1 a 10: "))

    # Verifica se a nota está dentro do intervalo permitido
if nota >= 7 and nota < 10:
    print("Aluna Aprovada")
elif nota >= 1 and nota < 7:
    print("Aluna Reprovada.")
else:
    print("Nota inválida. Por favor, insira uma nota de 1 a 10.")
    