'''nome = input('Qual o seu nome completo? ').strip()
qtd = len(nome) - len(' ')
print(nome.upper())
print(nome.lower())
print(qtd)
dividido = nome.split()
(dividido[0])
print(len(dividido[0]))'''

#resolução
nome = str(input('Qual é seu nome completo? ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}.format(nome.upper()))
print('Seu nome em minúscula é {}.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


