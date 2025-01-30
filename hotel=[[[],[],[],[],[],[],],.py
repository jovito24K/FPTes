# hotel=[[[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],],
#        [[],[],[],[],[],[],]]
# nombre=[]
# print("bienvenido")
# while True:
#     print("1-agendar habitacion\n2-ver estado hotel \n3-salir e inprimir boleta")
#     opc=int(input("ingrese una opcion"))
#     match opc:
#         case 1:
#             Piso=int(input("que piso desea agendar(1-10)"))
#             habi=int(input("que habitacion desea a(1-6)"))
#             nom=input("ingrese su nombre")
#             hotel[Piso-1][habi-1]=nom
#             for r in hotel:
#                 print(r)
#         case 2:
#             for i in hotel:
#                 if i!="":
#                     hotel[Piso-1][habi-1]=("ocupada")
#             for r in hotel:
#                 print(r)
#         case 3:
#             # print("gracias por venir a este hotel  su boleta es ")
#             for j in hotel:
#                 if j==None:
#                     hotel[Piso-1][habi-1]=("disponible")
#             for r in hotel:
#                 print(r)
#         case _:                          
#             print("ingrese una opcion valida")




hotel=[
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
       ]
t=0

while True:
    print("""
            1.- Agendar habitación
            2.- Ver estado hotel
            3.- Monetizar
            4.- Salir
          """)
    op=int(input("Seleccione una opcion "))
    match op:
        case 1:
            p=int(input("Que piso desea agentdar? (1-10)" ))-1
            h=int(input("Que habitacion desea agentdar? (1-6)" ))-1
            nom=input("ingrese su nombre")
            
            if not hotel[p][h]:
                hotel[p][h]=nom
            else:
                print(f"Estimado {nom}, la habitacion {p+1}{h+1} ya esta tomada")
                
            # print(hotel)
        case 2:
            for roro in hotel:
                print(roro)
        case 3:
                for i, piso in enumerate(hotel):
                    for j, habitacion in enumerate(piso):
                        if habitacion:
                            if i>=0 and i<=2:
                                t=t+78500
                            elif i>=3 and i<=6:
                                t=t+90000
                            elif  i>=7 and i<=9:
                                t=t+110000  
                print("el total es " , t*1.19)
        case 4:
            print("Saliendo del programa Hotel")
            break
    
        case _:
            print("No es ua opcion válida. seleccione del 1 al 3")