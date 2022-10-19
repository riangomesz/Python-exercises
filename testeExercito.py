# Programa que recebe a idade, o nome, a altura, o peso de um usuário. 
# E se for compatível com os requisitos para servir ao exército
# Fala para pessoa que está apta para servir, se não diz que não está apta para servir ao exército


idade = int(input())
nome = str(input())
altura = float(input())
peso = float(input())

if (idade >= 18 and peso >= 60 and altura >= 1.70):
     print("Você está apto a servir o exercito")
else:
     print ("Você não está apto a servir o exercito")

