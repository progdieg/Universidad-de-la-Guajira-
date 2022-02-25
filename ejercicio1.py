
# def main():
#     nombre= input("Digite el nombre:    ")
#     edad=int(input("Digite la edad:     "))

#     print(f"Mi nombre es {nombre} y mi edad es: {edad}")





# def calcularSueldo():
#     nombre=input("Digite el nombre del empleado: ")
#     salario=float(input("Digite el salario del empleado: "))
#     dias=int(input("Digite dias trabajados: "))


#     salario=((salario/30)*dias)
#     print(f"Nombre del empleado: {nombre}, el salario es de: {salario:0f} y los dias trabajados fueron:  {dias}")

# def main():
#     calcularSueldo()

# if __name__=="__main__":
#     main()
    




def calcularSueldo(salario, diasT):
    sueldoPagar= salario=((salario/30)*diasT)
    return sueldoPagar
    
# la variable salario y diasT tienen los mismos valores pero no son la misma variable 

#las constantes siempre van en mayusculas
   
def main():
    SALARIO_MIN =1000000
    SUB_ALIM=120000
    SUB_TRANSP=80000
    BONO=50000
    nombre=input("Digite el nombre del empleado: ")
    salario=float(input("Digite el salario del empleado: "))
    dias=int(input("Digite dias trabajados: "))
    sueldoPagar=calcularSueldo(salario, dias)

    if salario<(SALARIO_MIN*2):
        sueldoPagar=sueldoPagar+SUB_ALIM+SUB_TRANSP
    else:
        sueldoPagar=sueldoPagar+BONO

    print(f"Nombre del empleado: {nombre}, el salario es de: {sueldoPagar:.0f} y los dias trabajados fueron:  {dias}")


if __name__=="__main__":
    main()