# Programa que recebe um horário estabelecido pelo usuário, 
# E SOMA com os minutos também informado pelo mesmo.
# Retornando o horário em que o evento acaba.



hour = int(input("Hora inicial: "))
mins = int(input("Minutos iniciais: "))
dura = int(input("Duração do evento em minutos: "))

# Write your code here.
minutes = (mins + dura) % 60
hours = int(hour +(mins + dura)/ 60) % 24

print(hours,":",minutes)
