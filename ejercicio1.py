import random as rd
# 2.0,1.40,1.0,3.0,2.60
numeros  = input("Ingrese precios (separados por coma): ")
numerosL = numeros.split(",")
numerosAlea = rd.sample(numerosL, 3)
print("numerosAlea",numerosAlea)
#['2.60', '1.0', '2.0']
num1 = float(numerosAlea[0])
num2 = float(numerosAlea[1])
num3 = float(numerosAlea[2])
promedio = (num1+num2+num3)/3
print("promedio: ",promedio)






