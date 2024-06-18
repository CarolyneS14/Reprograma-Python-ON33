#Erro = (type error) TypeError: can only concatenate str (not "int") to str 
# a = "string" + 5
# print('O resultado e: ', a)

#correto
a = "string" + str(5)
print('O resultado e: ', a)
