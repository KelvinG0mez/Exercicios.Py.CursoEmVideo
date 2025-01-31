a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#VERIFICA QUAL É O MENOR, DEFINIMOS UM MENOR PARA ELIMINARMOS UMA ANALISE.
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#VERIFICA QUAL É O MAIOR, DEFINIMOS UM MAIOR PARA ELIMINARMOS UMA ANALISE.
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))