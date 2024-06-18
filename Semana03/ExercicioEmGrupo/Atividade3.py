# Crie um programa onde a usuária deve inserir uma nota de 1 a 10 e imprime se a aluna foi aprovada ou reprovada.
# A nota mínima para aprovação é 7. 
# Também é necessário que a aluna tenha uma frequência de 75% para ser aprovada.
# Ela pode ser aprovada por nota ou por frequência.

nota = float(input("Insira a nota da aluna (de 1 a 10): "))
frequencia = float(input("Insira a frequência da aluna (em porcentagem): "))

if nota >= 7 or frequencia >= 75:
    print("Aluna aprovada!")
else:
    print("Aluna reprovada.")
