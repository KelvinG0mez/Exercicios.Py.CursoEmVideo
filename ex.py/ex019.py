import random

pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
#fazemos uma pasta com os nomes dos alunos
alunos = [pa, sa, ta, qa]
#jogamos a pasta na variavel escolha, definimos aleatoria.escolha=random.choice
escolhido = random.choice(alunos)
print('o aluno escolhido foi {}'.format(escolhido))