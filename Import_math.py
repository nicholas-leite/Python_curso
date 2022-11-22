import math
''' Desafio 16 utilizar somente a parte inteira de um número real
#n1 = float(input('Digite um número:' ))
#print ('A parte inteira desse número é: {}'.format(math.trunc(n1)))'''

'''Desafio 17: Calcular a hipotenusa
ca = float (input('Digite o cateto adjacente: '))
co = float (input('Digite o cateto oposto: '))
print('A hipoteneusa do triângulo com cateto adjacente de tamanho {} e de cateto oposto {} é: {:.2f}'.format(ca,co,math.sqrt(pow(ca,2)+pow(co,2))))
h = math.hypot(ca.co)
'''
'''Desafio 18: Leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
n1 = float(input('Digite um ângulo:'))
seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O ângulo {}, possui seno {:.2f}, cosseno {:.2f} e tan {:.2f}!'.format(n1,seno,cos,tan))'''

#Desafio 19: Sorteando um item na lista
import random
'''a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
pessoas = [a1,a2,a3,a4]
sorteado = random.choice(pessoas)
print('O sorteado foi: {}'.format(sorteado))'''

'''Desafio 20 Criar uma lista ordenada de pessoas (sorteio)
import random
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
pessoas = [a1,a2,a3,a4]
random.shuffle(pessoas)
print('a lista é: {}'.format(pessoas))'''

#Desafio 21: Tocando MP3
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()


