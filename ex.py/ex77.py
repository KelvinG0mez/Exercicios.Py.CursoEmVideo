palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM",
            "PYHTON", "CURSO", "GRATIS",
            "ESTUDAR", "PRATICAR", "TRABALHAR",
            "MERCADO", "PROGRAMADOR", "FUTURO")

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos ", end=" ")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(f"{letra}", end=" ")
