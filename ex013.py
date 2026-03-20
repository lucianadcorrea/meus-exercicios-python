'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.
'''
salario=float(input('Qual o seu salário? R$ '))
novo_salario=salario+(salario*15/100)
print('Com o reajuste de 15%, seu novo salário é de R$ {:.2f}'.format(novo_salario))
