# Código que recebe a temperatura em Celsius e Fahrenheit
# Depois converte Fahrenheit para Celsius e vice e versa 


print("Celsius to Fahrenheit")

celsius = float(input("\nEnter the temperature in Celsius: "))
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

c_to_f = (celsius * (9/5))+ 32
f_to_c = (fahrenheit - 32)* 5/9

print("\n",celsius," Celsius to Fahrenheit is",round(c_to_f,2),"F")
print("\n",fahrenheit," Fahrenheit to Celsius is",round(f_to_c,2),"C")
