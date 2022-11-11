import math

print("----------------------------")
print("--- LLAMADA - TELEFÓNICA ---")
print("----------------------------")

#Input
M=int(input("Digite el tiemppo de duración de su llamada: "))

#Proseccing
if M>3:
    M= 300+(M-3)*50
else:
    M=300

#Output
print("---------RESULTADOS---------")
print("Valor a pagar: "+str(M))