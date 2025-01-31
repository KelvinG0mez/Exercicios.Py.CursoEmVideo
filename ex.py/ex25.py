nome = str(input('Qual é o seu nome: ')).strip().title()
divisão = nome.split()
print('Seu nome tem Silva?', end=' ')
print(('Silva' in divisão))

#OUTRA FORMA DE FAZER

'''nome = str(input('Qual é o seu nome? '))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))'''