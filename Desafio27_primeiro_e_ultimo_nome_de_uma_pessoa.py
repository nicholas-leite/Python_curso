nome_comp = str(input('Digite seu nome completo: ')).strip().upper()
n = nome_comp.split()
print('Muito prazer em te conhecer {}'.format(nome_comp))
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))
