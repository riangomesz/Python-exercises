# Programa que recebe o nome do eleitor, informa as informações dos candidatos e recebe o voto da pessoa


print("Eleições Brasil 2022")
print("Digite \n - Para votar no Bolsonaro do Partido Liberal aperte 22\n - Para votar no Lula do Partido dos Trabalhadores aperte 13 \n - Aperte 0, caso queire votar Nulo")

for  i in range(2):
    nome = str(input("\n Informe seu Nome:"))
    voto = int(input(" Informe seu voto:"))
    if voto == 22:
        print("Você votou no Bolsonaro.")
    elif voto == 13:
        print("Você votou no Lula.")
    elif voto == 0:
        print("Você anulou o seu voto")
    else:
        print("Digite algum dos números dos candidatos para votar.")

