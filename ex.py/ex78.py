valores = []

for posicao in range(0, 6):
    escolha = int(input(f"Digite um valor na posição {posicao}º: "))
    valores.append(escolha)

maior = max(valores)
menor = min(valores)

i_maior = [posicao for posicao, valor in enumerate(valores) if valor == maior]
i_menor = [posicao for posicao, valor in enumerate(valores) if valor == menor]

print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi o {maior} na posição {i_maior}º")
print(f"O menor valor digitado foi o {menor} na posição {i_menor}º")
