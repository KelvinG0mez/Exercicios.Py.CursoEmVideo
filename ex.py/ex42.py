a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
#ANALIZAMOS SE OS VALORES PODEM OU NAO FORMAR UM TRIANGULO.
if a + b > c and a + c > b or a + b == c and a + c == b:

    print('os segmentos PODEM FORMAR um triângulo ', end='')
#SE PUDEREM FORMAR UM TRIANGULO, ENTAO ANALIZAMOS QUE TIPO OS VALORES PODEM FORMAR.
    if a == b == c:
        print('EQUILATERO!')
    #QUANDO FAZEMOS O IGUAL(==) NAO PRECISAMOS ANALIZAR TODOS OS VALORES, POREM, A DIFERENÇA SIM.
    if a != b != c != a:
        print('ESCALENO!')
    #NAO ANALIZAMOS O ISOSCELES POIS, SE NAO É NENHUMA DAS OPCOES A CIMA SO PODE SER .
    else:
        print('ISOSCELES!')

else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')