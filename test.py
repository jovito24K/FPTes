from os import system
system("cls")
#EJERCICIO 1
# nombre = "el jovito "
# edad = 18
# print(f"mi nombre es {nombre} y mi edad es {edad} años " )

#EJERCICIO 2
# num1=int(input("ingrese un numero\n "))
# num2=int(input("ingrese otro numero\n "))
# print(num1+num2)

#EJERCICIO 3
# num1=int(input("ingrese un numero \n"))
# if num1>0:
#     print("el numero es positivo")
# else:
#     print("el numero es negativo o cero")

#EJERCCIO 4
# edad=int(input("ingre su edad\n"))
# if edad >=18:
#     print("usted es adulto")
# else:
#     print("usted es menor de edad")

#EJERCCIO 5

# num1=int(input("ingre el primer numero\n"))
# num2=int(input("ingre el segundo numero\n"))
# num3=int(input("ingre el tercer numero\n"))

# promedio= (num1+num2+num3)/3
# print(f"el promedio es {promedio}")

# EJERCICIO 6
# cantidadEntrada=int(input("ingrese cuantas entradas desea comprar \n"))
# valor=0
# for i in range(cantidadEntrada):
#     edad=int(input("ingre su edad\n"))
#     if edad <=12:
#         print("su entrada es de $500")
#         valor+=500
#     else:
#         if edad >12 and edad <18:
#             print("su entrada es de $1000")
#             valor+=1000
#         else:
#             if edad>=19 and edad <64:
#                 print("su entrada es de 2000")
#                 valor+=2000
#             else:
#                 print("su entrada es de 700")
#                 valor+=700
# print(f"el total de su compra es {valor}")

#EJERCICIO 7
# total=25000
# ubi=input("pertenece a la florida\n")
# if ubi == "si":
#     carnet=input("tiene carnet de socio\n")
#     if carnet == "si":
#         socio=int(input("ingrese su numero\n"))
#         jubilado=(input("es jubilado"))
#         if jubilado=="si":
#             print(f"su total a pagas es {total*0.75}")
#         else:
#             print(f"su total a pagar es {total}")
#     else:
#         print("cree su carnet aca")
    
#         nombre=input("ingrese su nombre\n")
#         Rut=int(input("ingrese su rut sin gion\n"))
#         telef=int(input("ingrese su numero de telefono\n"))
#         print("carnet creado correctamente")
#         jubilado=(input("es jubilado\n"))
#         if jubilado=="si":
#             print(f"su total a pagas es {total*0.75}")
#         else:
#             print(f"su total a pagar es {total}")
# else:
#     print("gracias por la visita")