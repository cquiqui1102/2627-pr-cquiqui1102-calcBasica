# Desarrolla un programa que en Python que solicite dos números decimales y muestre el resultado de las cuatro operaciones aritméticas básicas:
# suma, resta, multiplicación y división.

def sumar(numero1: float, numero2: float) -> float:
    """
    Calcula la suma de los dos números

    Args:
    numero1: primer número a sumar
    numero2: segundo número a sumar

    Returns:
    El resultado de la suma
    
    """
    suma: float= numero1 + numero2
    return suma


def restar(numero1: float, numero2: float) -> float:
    """
    Calcula la resta de los dos números

    Args:
    numero1: primer número a restar
    numero2: segundo número a restar

    Returns:
    El resultado de la resta
    
    """
    resta: float= numero1 - numero2
    return resta


def multiplicar(numero1: float, numero2: float) -> float:
    """
    Calcula la multiplicación de los dos números

    Args:
    numero1: primer número a multiplicar
    numero2: segundo número a multiplicar

    Returns:
    El resultado de la multiplicación
    
    """
    multiplicacion: float= numero1 * numero2
    return multiplicacion


def dividir(numero1: float, numero2: float) -> float: 
    """
    Calcula la división de los dos números, si el divisor es 0 la división no será válida

    Args:
    numero1: dividendo
    numero2: divisor

    Returns:
    El resultado de la división
    
    """
    if numero2 != 0:
        division: float= numero1 / numero2
        return division
    else:
        return "no válida"

def main():
    """
    Función principal
    
    Args:
    numero1: primer numero para calcular
    numero2: segundo numero para calcular

    Returns:
    Suma, Resta, Multiplicación, División
    
    """

    # Entrada
    numero1 = float(input("Introduzca un primer número: "))
    numero2 = float(input("Introduzca un segundo número: "))

    # Salida
    print(f"Los cálculos con los siguientes números ({numero1} y {numero2}) son: ")
    print(f"Suma: {sumar(numero1, numero2)}")
    print(f"Resta: {restar(numero1, numero2)}")
    print(f"Multiplicación: {multiplicar(numero1, numero2)}")
    print(f"División: {dividir(numero1, numero2)}")
    
if __name__ == "__main__":
    main()