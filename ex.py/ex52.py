cont = 0

n = int(input('Digite um numero: '))

for c in range(1, n+1):

    if n % c == 0:
       print('\033[33m',end=' ')
       cont += 1
    else:
        print('\033[31m',end=' ')
        
    print('{}'.format(c), end=' ')

print('\n\033[mO numero {} é foi divisivel {} vezes'.format(n, cont, ))

if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
