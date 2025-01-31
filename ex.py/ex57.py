sexo = str(input('Informe seu sexo [M/F]: ')).strip().lower()[0]

while sexo not in 'MmFf':
    sexo = str(input('DADO INVALIDO! Por favor, informe seu sexo novamente: ')).strip().lower()[0]

print('Sexo registrado com sucesso')
