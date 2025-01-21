from os import system
system("cls")

valor=0
valoriva=0
total=0
iva=1.19
debito=1.015
credito=1.0289
iva2=0

cantidad1=0
cantidad2=0
cantidad3=0
cantidad4=0
producto1=0
producto2=0
producto3=0
producto4=0


cocacola=800
pepsi=900
agua=1000
fanta=1200

print("bienvenido que desea comprar")
while True:
    print("1- coca cola $ 800\n 2- pepsi $ 900\n 3- agua vital $ 1000\n 4- fanta $ 1200\n 5- pagar\n 6-mostrar boleta")

    opc=int(input("que desea comprar "))
    match opc:
        case 1:
            cantidad1 = int(input("¿Cuántas Coca Colas desea comprar? "))
            cocacola += cantidad1
            valor += cantidad1 * 800
            valoriva += cantidad1 * 800
            iva2=valoriva-valoriva
            producto1= valoriva
        case 2:
            cantidad2 = int(input("¿Cuántas Pepsi desea comprar? "))
            pepsi += cantidad2
            valor += cantidad2 * 900
            valoriva += cantidad2 * 900
            iva2=valoriva-valoriva
            producto2=valoriva

        case 3:
            cantidad3 = int(input("¿Cuántas Agua Vital desea comprar? "))
            agua += cantidad3
            valor += cantidad3 * 1000
            valoriva += cantidad3 * 1000
            iva2=valoriva-valor
            producto3=valoriva

        case 4:
            cantidad4 = int(input("¿Cuántas Fanta desea comprar? "))
            fanta += cantidad4
            valor += cantidad4 * 1200
            valoriva += cantidad4 * 1200
            iva2=valoriva-valor
            producto4=valoriva



        case 5:
            pago = int(input("Ingrese qué sistema de pago desea:\n1- Efectivo\n2- Débito\n3- Crédito "))
            match pago:
                case 1:
                    print(f"El monto a pagar es: {valor} ")
                    break

                case 2:
                    valoriva = valoriva * iva
                    iva2=valoriva-valor
                    total = valoriva*debito
                
                case 3:
                    valoriva = valoriva * iva
                    iva2=valoriva-valor
                    total=valoriva*credito
                case _:
                    print("ingrese una opcion valida")
        case 6:
            print(" boleta")
            if producto1 >0:
                print(f"producto  coca cola")
                print(f"la cantidad que lleva es {cantidad1}")
            if producto2 >0:
                print(f"producto  pepsi")
                print(f"la cantidad que lleva es {cantidad2}")
            if producto3 >0:
                print(f"producto  agua mineral")
                print(f"la cantidad que lleva es {cantidad3}")
            if producto4 >0:
                print(f"producto  fanta")
                print(f"la cantidad que lleva es {cantidad4}")

            print(f"Total sin IVA: {valor}")
            print(f"Valor con IVA: {valoriva}")
            print(f"IVA: {iva2}")
            print(f"Total a pagar: {total}")
            break

        case _:
            print("ingrese una opcion valida")

                


# from os import system
# system("cls")
# import time
# c=0
# h=0
# ch=0
# ca=0
# ra=0
# total=0
# total2=0
# total3=0
# while True:
#     print("bievenido al merka do")
#     print("1.- Comprar")
#     print("2.- Pagar")
#     print("3.- Salir")
#     opc=int(input(">>> "))
#     system("cls")
#     if opc==1:
#         while True:
#             print("que desea comprar")
#             print("1.- caco cola $1500")
#             print("2.- helado $2500")
#             print("3.- chocolate $1000")
#             print("4.- carne $5500")
#             print("5.- ramias $1500")
#             print("6.- volver al inicio")
#             op=int(input(">>> "))
            
#             if op ==1:
#                 print(" se agrego caco cola $1500")
#                 total=total+1500
#                 c=c+1
#                 input("presione enter")
#                 system("cls")
#             elif op ==2:
#                 print("se agrego helado $2500")
#                 total =total+2500
#                 h=h+1
#                 input("presione enter")
#                 system("cls")
#             elif op ==3:
#                 print("se agrego chocolate $1000")
#                 total=total+1000
#                 ch=ch+1
#                 input("presione enter")
#                 system("cls")
#             elif op ==4:
#                 print("se agrego carne $5500")
#                 total=total+5500
#                 ca=ca+1
#                 input("presione enter")
#                 system("cls")
#             elif op ==5:
#                 print("se agrego ramias $1500")
#                 total=total+1500
#                 ra=ra+1
#                 input("presione enter")
#                 system("cls")
#             elif op ==6:
#                 print("volviendo al inicio")
#                 time.sleep(1)
#                 system("cls")
#                 break
#             else:
#                 print("opcion invalida")
#     elif opc ==2:
#         print("esta pasando por caja")
#         print(f"su total es de ${total}")
#         total2=total*1.19
#         print(f"su total con el iva incluido es de {total2}")
#         input("presione enter para pagar")
#         system("cls")
#         while True:
#             print("con que desea pagar?")
#             print("recuerde que cada metodo de pago tiene una comision")
#             print("1.- efectivo + 0%")
#             print("2.- debito + 1,5%")
#             print("3.- credito + 2,89%")
#             opp=int(input(">>> "))
#             time.sleep(1)
#             system("cls")
#             if opp==1:
#                 print("se secciono efectivo")
#                 print(f"su total es de {total2}")
#                 input("presione enter para volve al inicio")
#                 system("cls")
#                 break
#             elif opp==2:
#                 print("se secciono debito")
#                 total2=total2*1.5
#                 print(f"su total es de {total2}")
#                 input("presione enter para volve al inicio")
#                 system("cls")
#                 break
#             elif opp==3:
#                 print("se secciono credito")
#                 total2=total2*2.89
#                 print(f"su total es de {total2}")
#                 input("presione enter para volve al inicio")
#                 system("cls")
#                 break
#             else:
#                 print("opcion invalida\n")
#     elif opc==3:
#         total3=total2-total
#         print("gracias por su visita\n")
#         print("------------------------------------")
#         print(f"caco cola {c}")
#         print(f"helado $2500 {h}")
#         print(f"chocolate $1000 {ch}")
#         print(f"carne $5500 {ca}")
#         print(f"ramias $1500 {ra}")
#         print("------------------------------------")
#         print(f"Subtotal ${total}, IVA ${total3} TOTAL ${total2}\n")
#         break
#     else:
#         print("opcion invalida\n")