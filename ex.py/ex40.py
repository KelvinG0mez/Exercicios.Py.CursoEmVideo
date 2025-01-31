nota1 = float(input('Qual a priemira nota? '))
nota2 = float(input('Qual a segunda nota? '))

media = (nota1 + nota2) / 2

print('Tirando {} e {}, a media do aluno é {:.1f}'.format(nota1, nota2, media))

if media >= 7:
    print('APROVADO!!')

elif media >= 5 or media <= 6.9:
    print('RECUPERAÇÃO!!')

else:
    print('REPROVADO!!')



