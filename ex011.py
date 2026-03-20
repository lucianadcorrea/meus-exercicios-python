'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

larg=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{}m e sua área é {:.2f}m²'.format(larg, alt, larg*alt))
print('Para pintar essa área de {:.2f}m², você vai precisar de {:.2f}l de tinta'.format(larg*alt, (larg*alt)/2))