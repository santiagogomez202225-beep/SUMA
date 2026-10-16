def sumar(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = sumar(num1, num2)
    print(f"La suma de {num1} + {num2} = {resultado}")