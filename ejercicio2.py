def calcularSueldo():
    nombre=input("Digite el nombre del empleado: ")
    salario=float(input("Digite el salario del empleado: "))
    dias=int(input("Digite dias trabajados: "))


    salario=((salario/30)*dias)
    print(f"Nombre del empleado: {nombre} el salario es de: {salario:.0f} y sus dias fueron:  {dias}")

def main():
    calcularSueldo()

if __name__ == "__main__":
    main()