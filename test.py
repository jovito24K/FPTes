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
#     edad=int(input("ingre su edad para comprar la entrada\n"))
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
# print(f"el total de su compra es {valor} disfrute ")

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


# CICLO FOR
# TABLAS DE MULTIPLICAR
# for j in range(10):
#     for i in range(10):
#         print(j+1,"x", i+1,"=",(i+1)*(j+1))



# for i in range(18):
#     print(f"usted tiene {i+1} años ")
    
    


# promedio=0
# for i in range(3):
#     num=int(input("ingrese los numero "))
#     promedio=promedio+num
# print ("su promedio es ", promedio/(i+1))



# PAR INPAR
# num=10
# if num%2==0:
#     print("el numero es par")
# else:
#     print("el numero es inpar")

    
# MOSTRAR LOS NUMEROS INPARES
# num=int(input("ingrese un numero "))
# for i in range(num+1):
#     if i%2!=0:
#         print("los numeros inpar son",i)


# pal="hola"
# print(len(pal))
# for i in pal:
#     print(i)

# total=0
# pal=input("ingrese su nombre\n")
# print("la cantidad de letras es :",len(pal))
# for i in range(len(pal)):
#     print(i+1)
#     total=total+(i)
# print("la suma de la cantidad de letras es ",total+i+1)

# LISTAS
# contraCorrecta=11234
# for i in range(3):
#     contra=int(input("ingrese la contraseña"))
#     if contra==contraCorrecta:
#         print("la contraseña es correcta bienbenido")
#         break
#     else:
#         print("incorrecto intente nuevamente")

# num=12
# for i in range(5):
#     contra=int(input("adivina el numero del 1 al 100 \n"))
#     if contra <num:
#         print("ingrese un numero mas alto\n")
#     if contra >num:
#          print("ingrese un numero mas bajo\n")
#     if contra == num:
#         print("el numero es correcto")
#         break



# num=int(input("jugador uno ingrese un numero\n"))
# intentos=int(input("cuantos intentos quieres para el jugador dos\n"))
# system("cls")
# for i in range(intentos):
#     contra=int(input(" jugador dos adivina el numero del 1 al 100 \n"))
#     if contra <num:
#         print("ingrese un numero mas alto\n")
#     if contra >num:
#          print("ingrese un numero mas bajo\n")
#     if contra == num:
#         print("el numero es correcto")
#         break
