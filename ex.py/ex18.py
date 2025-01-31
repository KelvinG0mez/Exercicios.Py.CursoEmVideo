import math

n1 = float(input('Digite o angulo que você deseja: '))

n2 = math.sin(math.radians(n1))
n3 = math.cos(math.radians(n1))
n4 = math.tan(math.radians(n1))

print('''O angulo de {} tem;\nSENO de {:.2f}\nCOSSENO de {:.2f}
TENGENTE de {:.2f}'''.format(n1, n2, n3, n4))