#nome = input("qual o seu nome? ")
# print('Prazer em te conhecer {:20}!'.format(nome)) fica com 20 carecteres, como nome a esquerda
# print('Prazer em te conhecer {:>20}!'.format(nome)) sinal de maior fica a direita
# print('Prazer em te conhecer {:^20}!'.format(nome)) fica centralizado
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s=n1+n2
m= n1*n2
d=n1/n2
di= n1//n2
e=n1**n2
# print('A soma vale {},o produto é {} e a divisão é {:.3f}'.format(s,m,d))
# print('divisão inteira {} e potência {}'.format(di,e))
print('A soma vale {},\n o produto é {} \n e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('divisão inteira {} e potência {}'.format(di,e))