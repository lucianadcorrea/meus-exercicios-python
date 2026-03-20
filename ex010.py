'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
'''
dinheiro=float(input('Quanto dinheiro tem na sua carteira? R$ '))
print('Convertendo R$ {:.2f} para dólar, você tem U$D {:.2f}'.format(dinheiro,dinheiro/5.22))