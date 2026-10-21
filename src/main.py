# Desarrolla un programa que en Python que solicite dos números decimales y muestre el resultado de las cuatro operaciones aritméticas básicas:
# suma, resta, multiplicación y división.

def sumar(numero1: float, numero2: float) -> float:
    """
    Calcula la suma de ambos números.

    Args:
    numero1: Primer número para sumar
    numero2: Segundo número para sumar

    Returns:
    float = Suma
    
    """

    suma: float = numero1 + numero2
    return suma



def restar(numero1: float, numero2: float) -> float:
    """
    Calcula la resta de ambos números.

    Args:
    numero1: Primer número para restar
    numero2: Segundo número para restar

    Returns:
    float = Resta
    
    """

    resta: float = numero1 - numero2
    return resta



def multiplicar(numero1: float, numero2: float) -> float:
    """
    Calcula la suma de ambos números.

    Args:
    numero1: Primer número para multiplicar
    numero2: Segundo número para multiplicar

    Returns:
    float = Multiplicación
    
    """

    multiplicacion: float = numero1 * numero2
    return multiplicacion



def dividir(numero1: float, numero2: float) -> float:
    """
    Calcula la suma de ambos números.

    Args:
    numero1: Dividendo
    numero2: Divisor

    Returns:
    float = División
    
    """
    if numero2 != 0:
        division = numero1 / numero2
        return division
    else:
        return "no válida"



def main():
    """
    Función principal
    
    Args:
    Primer número para calcular
    Segundo número para calcular
    
    Returns:
    Suma
    Resta
    Multiplicación
    División

    """

    # Entrada

    numero1 = float(input("Introduzca el primer número a calcular: "))
    numero2 = float(input("Introduzca el segundo número a calcular: "))

    # Salida
    
    print(f"Los cálculos con los siguientes números ({numero1} y {numero2}) son: ")
    print(f"Suma: {sumar(numero1, numero2)}")
    print(f"Resta: {restar(numero1, numero2)}")
    print(f"Multiplicación: {multiplicar(numero1, numero2)}")
    print(f"División: {dividir(numero1, numero2)}")
    
if __name__ == "__main__":
    main()