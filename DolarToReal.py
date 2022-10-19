# Programa que recebe um valor em USD e em BRL 
# Depois ele converte baseando-se na cotação do dia 19/10/2022


print("Conversor de Dólar para Real")


qtde_dolar = float(input("\nUSD:"))
qtde_real = float(input("R$:"))

dolar_to_real = qtde_dolar * 5.29
real_to_dolar = qtde_real * 0.19

print("$",qtde_dolar,"dolars é",round(dolar_to_real, 2),"reais")
print("R$",qtde_real,"reais é",round(real_to_dolar, 2),"dolars")
