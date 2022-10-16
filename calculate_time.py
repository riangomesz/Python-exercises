hour = int(input("Hora inicial: "))
mins = int(input("Minutos iniciais: "))
dura = int(input("Duração do evento em minutos: "))

# Write your code here.
minutes = (mins + dura) % 60
hours = int(hour +(mins + dura)/ 60) % 24

print(hours,":",minutes)
