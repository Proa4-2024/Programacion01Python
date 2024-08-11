frase=input("ingresa la frase")
contador=0

for i in frase:
    if i in "aeiouAEIOU":
        contador=contador+1
print("la cantidad de vocales son:",contador)
