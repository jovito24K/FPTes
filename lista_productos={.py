# lista_productos={
#     'frutas':{
#         'uva': 1800, 'manzana':2100
#     },
#     'Verduras':{
#         'apio': 900, 'lechuga': 1300
#     },
#     'Cereales':{
#         'Chocapic':4800, 'Zucaritas': 5200
#     },
#     'Carnes':{
#         'Puerco':8990, 'Vacuno': 13000
#     }
# }
# print( lista_productos['Cereales']['Zucaritas'])
# for key  in lista_productos:
#     print(key, '', lista_productos[key])

# for key  in lista_productos:
#     print(key, ":")
#     for ll in lista_productos[key]:
#         print(ll, ':', lista_productos[key][ll]  )

# frutas={
#         'uva': 1800, 'manzana':2100
#     }
# frutas["sandia"] = 5490
# frutas["pera"] = 1800
# frutas["uva"] = 2000
# print(frutas) 




# nom=[]
# while True:
#     nomb=input("ingrese su nombre ")
#     nom.append(nomb)
#     eda=int(input("ingrese su edad "))
#     nom.append(eda)
#     salir=input("para salir precione x para continuar precione enter ")
#     if salir =="x":
#         break
#     else:
#         print("siga ingresando numbres")
# with open("mi_archivo.txt","w") as archivo:
#     archivo.write("hola este es mi archivo txt perro \n")

import json

personas = {}

while True:
    nomb = input("Ingrese su nombre: ")
    eda = int(input("Ingrese su edad: "))
    personas[nomb] = eda
    
    salir = input("Para salir presione 'x', para continuar presione enter ")
    if salir == "x":
        break
    else:
        print("Siga ingresando nombres y edades.")

print("Lista de personas ingresadas:")
for nombre, edad in personas.items():
    print(f"Nombre: {nombre}, Edad: {edad} años")

with open("archivo. json","w") as archivo:
    json.dump(personas,archivo)
