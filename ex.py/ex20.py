#filtramos apenas oque queria, de random importe apenas shuffle
from random import shuffle

pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('quarto aluno: ')

alunos = [pa, sa, ta, qa]
#shuffle=embaralhar(alunos)
shuffle(alunos)
print('''A ordem da apresentação será: 
{}'''.format(alunos))