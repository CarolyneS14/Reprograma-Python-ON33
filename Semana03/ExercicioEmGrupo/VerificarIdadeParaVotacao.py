# Solicitação da idade do usuário e chamada da função        
idade = input('Digite a sua idade: ')

# Função para verificar se a pessoa pode votar
try:
# Converte a entrada para um número inteiro
    idade = int(idade)
# Verifica a idade e imprime o resultado
    if idade <= 16:
        print('Você não pode votar!')
    else:
        print('Você ja pode votar.')
except ValueError:
    print('Idade inválida.')
