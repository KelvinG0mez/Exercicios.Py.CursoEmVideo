larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg*alt
litr = area / 2

print('A sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(litr))