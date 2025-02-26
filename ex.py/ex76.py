itens = (
                "lapis", 1.75,
                "Borracha", 2,
                "Caderno", 15.90,
                "Estojo", 25.00,
                "Transferidor", 4.20,
                "Compasso", 9.99,
                "Mochila", 120.30,
                "Caneta", 22.30,
                "Livro", 34.90,
                "Apontador", 5.50
)

print("-"*45)
print("LISTAGEM DE PREÇOS".center(44))
print("-"*45)

for posicao in range(0, len(itens)): # aqui pedimos para mostrar tudo na posicao 0 ate o fim da tupla usando len
    if posicao % 2 == 0: # se posicao estiver em um indice par, ele é o item
      print(f"{itens[posicao]:.<35}", end='')# chamamos o item, alinhamos 35 casas a direita
    else:# se estiver no indice impar, ele é o preço
      print(f"R${itens[posicao]:>7.2f}")# chamamos o preço, alinhamos 7 casas a esquerda

print("-"*45)
