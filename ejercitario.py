while(True):
    ejercicio = int(input(f"""
Ingrese un numero del 1 al 5 dependiendo de que ejercitario desea probar, 
    o 0 si desea salir:  
"""))
    
    if ejercicio == 1:
        print(f"""1- Escribir un programa que nos calcule el
cuadrado de los 9 primeros números naturales
(utiliza la estructura for)
""")
        for i in range(9):
            print(f"""
El cuadrado de {i} es igual a: {i**2}
""")
            
    elif ejercicio == 2:
        print(f"""
2- Se pide escribir un programa que nos calcule la
suma de los 4 primeros números pares desde
un número que introducimos por teclado. Es
decir, si insertamos un 5, nos haga la suma de
6+8+10+12              
""")
        from utils.functions import suma_par
        numero = int(input("Ingrese un numero aleatorio: "))

        resultado = suma_par(numero)
        print(f"""La suma de los 4 primeros números pares desde el {numero} es de: {resultado}
        """)

    elif ejercicio == 3:
        print(f"""
3- Cargar una lista de N numeros, sumar sus
componentes e imprimir la suma y el promedio
de los números.
""")
        lista = []
        tope = int(input(("Ingrese un numero cualquiera: ")))
        tope = tope + 1
        suma = 0
        contador = 0
        for i in range(tope):
            suma += i
            contador += 1  
            lista.append(i)
        print(f"""
lista generada a partir del numero ingresado es:
{lista},
la suma total de la lista es de: {suma}
la cantidad de elementos es de: {contador}
y el promedio de la lista es de: {suma/contador}              
""")
        
    elif ejercicio == 4:
        print(f"""
4- Cargar una lista con N numeros y luego hallar
el promedio de los elementos en él que no
sean cero.
""")

        from utils.functions import par_impar

        numero = int(input("Ingrese la cantidad de valores a ingresar a la lista: "))

        par_impar(numero)
        
    elif ejercicio == 5:
        print(f"""
5- Cargar una lista de N componentes. Hallar e
imprimir el promedio de los valores impares.              
""")
        
        from utils.functions import suma_impar

        numero = int(input("Ingresa el total de elementos para la lista: "))
        suma_impar(numero)

    elif ejercicio == 0:
        exit()

    else:
        print(f"""
El valor ingresado es incorrecto!             
""")
