def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def divisiones(a,b):
    if b !=0:
        return a/b
    else:
        return("Error no se puede dividir por 0")

numero1=10
numero2=5

print("suma",suma(numero1,numero2))
print("resta",resta(numero1,numero2))
print("multiplicacion",multiplicacion(numero1,numero2))
print("division",divisiones(numero1,numero2))
