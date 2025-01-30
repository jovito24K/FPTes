



boleta=[]
dinero=0
producto=[["arroz a la francesa",4500],
          ["arroz a la marinera",5200],
          ["sopa marinera",9700]]

print("HOLA BIENBENIDO")
while True:
    print("1- ingrese su nombre")
    print("2- menu de platos con sus precios")
    print("3- mostrar saludo al cliente")
    print("4- salir del programa")
    opc=int(input("ingre las opciones en orden "))

    if opc ==1:
        nombre=input("INGRESE SU NOMBRE\n")
        boleta.append(nombre)
    else:
        if opc == 2:
            while True:
                print("1- arroz a la francesa   $4500")
                print("2- arroz marinero        $5200")
                print("3- sopa marinera         $9700")
                print("4- salir")
                opc=int(input("elige que plato deseas\n"))
                if opc == 1:
                    dinero1=dinero+4500
                    arroz=("arroz a la francesa")
                    boleta.append((arroz,dinero1))
                if opc == 2:
                    dinero2=dinero+5200
                    arrozM=("arroz marinero")

                    boleta.append((arrozM,dinero2))
                if opc == 3:
                    dinero3=dinero+9700
                    sopa=("sopa marinera")

                    boleta.append((sopa,dinero3))
                if opc == 4:
                    ("salir")
                    break
                else:
                    print("la opcion no esta disponible")      
        else:
            if opc ==3:
                print(f"gracias {nombre} por venir al restorant panuchis su total es {dinero}")
            else:
                if opc == 4 :
                    print(boleta)
                break
with open("mi_archivo.txt","w") as archivo:
    for i in boleta:
        archivo.write(f"{i}\n")

