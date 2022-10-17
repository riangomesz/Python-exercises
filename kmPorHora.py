# Programa que calcula o tempo estimado em horas 
# A partir da distância em km informada
# E da velocidade média km/h


distancia = float(input("Digite a distância em km:"))
velocidade = float(input("Digite a velocidade média em km/h:"))

tempo = distancia/velocidade

print("O tempo estimado é de %5.2f horas" % tempo)
