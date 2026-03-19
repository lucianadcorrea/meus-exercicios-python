"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
e milímetros.
"""
n=float(input('Digite a medida em metros: '))
print('A medida {}m, convertida em: \ncentimetros é {}cm \nmilímetros é {}mm'.format(n,n*100,n*1000))