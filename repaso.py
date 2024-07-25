# Función
#saludo="Hola"
#nombre="Paloma"
#apellido="Carranza"

#def concatenar (a,b,c):
 #   d= a+ " "+b+ " "+c 
  #  return d

#print (concatenar(saludo,nombre,apellido))


# Ciclo for y condicionales
print("Este programa cuenta la cantidad de letras")
palabra= input("Ingrese la frase o palabra: ")
contador= 0

for i in palabra:
    #contador= contador+1
    #print(i, end = "-")
    if i=="a":
        i="A"
        print(i, end= "")
    elif i=="e":
        i="E"
        print(i, end= "")
    elif i=="i":
        i="I"
        print(i, end= "")
    elif i=="o":
        i="O"
        print(i, end= "")
    elif i=="u":
        i="U"
        print(i, end= "")
    else:
        print(i, end="")
    


#print(f"Su frase tiene {contador} letras")
