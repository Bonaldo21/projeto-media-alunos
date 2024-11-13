print("Oi, tudo bem? Vou calcular a media para voce!")
n1 = float(input("Me fale sua primeira média: "))
n2 = float(input("Me fale sua segunda média: "))
n3 =float(input("Me fale sua terceira média: "))
media = n1 + n2 +n3 
mediat = media/3
print(f"Sua média é {mediat}")
if mediat >= 6.0:
    print("Voce passou! ")
elif mediat >= 5.0 and mediat < 6.0:
    print("Voce ficou de recuperação!")

else:
    print("Voce foi reprovado!")