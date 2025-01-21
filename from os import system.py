from os import system
system("cls")

valor = 0
valoriva = 0
total = 0
iva = 1.19
debito = 1.015
credito = 1.0289
iva2 = 0

cantidad1 = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0

cocacola = 0
pepsi = 0
agua = 0
fanta = 0

print("Bienvenido, ¿qué desea comprar?")
while True:
    print("1- Coca Cola $800\n2- Pepsi $900\n3- Agua Vital $1000\n4- Fanta $1200\n5- Pagar\n6- Mostrar boleta")

    opc = int(input("¿Qué desea comprar? "))
    match opc:
        case 1:
            cantidad1 = int(input("¿Cuántas Coca Colas desea comprar? "))
            cocacola += cantidad1
            valor += cantidad1 * 800
            valoriva += cantidad1 * 800

        case 2:
            cantidad2 = int(input("¿Cuántas Pepsi desea comprar? "))
            pepsi += cantidad2
            valor += cantidad2 * 900
            valoriva += cantidad2 * 900

        case 3:
            cantidad3 = int(input("¿Cuántas Agua Vital desea comprar? "))
            agua += cantidad3
            valor += cantidad3 * 1000
            valoriva += cantidad3 * 1000

        case 4:
            cantidad4 = int(input("¿Cuántas Fanta desea comprar? "))
            fanta += cantidad4
            valor += cantidad4 * 1200
            valoriva += cantidad4 * 1200

        case 5:
            pago = int(input("Ingrese qué sistema de pago desea:\n1- Efectivo\n2- Débito\n3- Crédito "))
            match pago:
                case 1:
                    total = valor
                    print(f"El monto a pagar en efectivo es: {total} ")
                    break

                case 2:
                    valoriva = valor * iva
                    total = valoriva
                    iva2 = valoriva - valor
                    print(f"El monto a pagar con débito es: {total}")
                    break

                case 3:
                    valoriva = valor * iva
                    total = valoriva
                    iva2 = valoriva - valor
                    print(f"El monto a pagar con crédito es: {total}")
                    break
                case _:
                    print("Ingrese una opción válida")

        case 6:
            print("Boleta de compra:")
            if cocacola > 0:
                print(f"Coca Cola: {cocacola} unidades")
            if pepsi > 0:
                print(f"Pepsi: {pepsi} unidades")
            if agua > 0:
                print(f"Agua Vital: {agua} unidades")
            if fanta > 0:
                print(f"Fanta: {fanta} unidades")

            print(f"Total sin IVA: {valor}")
            print(f"Valor con IVA: {valoriva}")
            print(f"IVA: {iva2}")
            print(f"Total a pagar: {total}")
            break

        case _:
            print("Ingrese una opción válida")

