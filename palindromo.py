# Programa que recebe uma palavara, e diz se a palavra digitada forma um palindromo ou não.
# Também retorna ao usuário a mesma escrita de trás pra frente e da forma normal.


frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
print("Você digitou {} ".format(palavras))
junto = " ".join (palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
if inverso == junto:
  print("Palindromo")
else:
  print("Não formou um Palindromo")
print(junto, inverso)
