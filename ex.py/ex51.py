
print('  10 TERMOS DE UMA PA')
print('='*24)

primeiro =  int(input('Primeiro termo: '))
razao = int(input('Razão: '))
#PARA CALCULARMOS O N-NEZIMO TERMO DE UMA PA TEMOS UMA FORMULA A SEGUIR
#COMO QUEREMOS APENAS OS 10 TERMOS DA PA, COLOCAMOS (10 - 1)
decimo = primeiro + (10 - 1) * razao

for PA in range(primeiro, decimo + razao, razao):
    print('{}>'.format(PA), end=' ')

print('ACABOU')

