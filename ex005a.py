n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
sub=n1-n2
mult=n1*n2
di=n1/n2
pot=n1**n2
dit=n1//n2
rest=n1%n2
print('soma {},\nsubstração {},\nmultuplicação {},\ndivisão {:.2f},\npotenciação {},\ndivisão inteira {},\nresto da divisão {}'.format(s,sub,mult,di, pot, dit, rest))