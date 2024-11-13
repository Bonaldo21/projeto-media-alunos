print("Oi, tudo bem? Vou calcular a media para voce!")
n1 = float(input("Me fale sua primeira média: "))
n2 = float(input("Me fale sua segunda média: "))
n3 =float(input("Me fale sua terceira média: "))
media = n1 + n2 +n3 
mediat = media/3
print(f"Sua média é {mediat}")
if mediat >= 6:
    print("Voce passou! ")
else:
    print("Voce foi reprovado!")