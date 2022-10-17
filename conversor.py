
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

total = dias * 24 * 3600 + horas * 3600 + minutos * 60
print("Convertido em segundos é igual a %10d segundos." %total)