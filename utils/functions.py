def suma_par(numero):
    suma = 0
    contador = 0
    numero_actual = numero + 1

    while contador < 4:
        if numero_actual % 2 == 0:
            print("Numero par encontrado: ",numero_actual)
            suma += numero_actual
            contador += 1
        numero_actual += 1

    return suma

def par_impar(numero):
    par = []
    impar = []
    ceros = 0
    contador = 0
    suma = 0
    for i in range(numero):
        valor = int(input(("Ingresa un numero: ")))
        if valor == 0:
            ceros +=1 
        elif valor % 2 == 0:
            contador += 1
            suma += valor
            par.append(valor)
        else:
            contador += 1
            suma += valor
            impar.append(valor)
    promedio = suma / contador       
    print(f"""
Numeros pares ingresados: {par} 
Cantidad total: {len(par)}
Numeros impares ingresados: {impar} 
Cantidad total: {len(impar)}
Cantidad total de ceros ingresados: {ceros} 
El promedio entre los numeros ingresados excluyendo los ceros "{contador}" por la suma total "{suma}" 
es de: {promedio}         
""")
    return par, impar, ceros


def suma_impar(numero):
    impar = []
    suma = 0
    contador = 0

    while contador < numero:
        valor = int(input("Ingresa un valor: "))
        if not valor % 2 == 0:
            impar.append(valor)
            suma += valor
        contador += 1
    cant_imp = len(impar)
    promedio = suma / cant_imp
    print(f"""
Valores impares ingresados: {impar}
Total de valores: {cant_imp}
El promedio de los valores impares ingresados es de: {promedio}
""")

    return suma