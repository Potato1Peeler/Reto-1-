print("Calculadora Simple")
    
num1 = float(input("Ingrese un numero: "))
operacion = input("Ingrese un operador (+ - * /): ")
num2 = float(input("Ingrese un segundo numero: "))
    
if operacion == '+':
    resultado = num1 + num2
    print("Resultado: ",resultado)
if operacion == '-':
    resultado = num1 - num2
    print("Resultado: ",resultado)
if operacion == '*':
    resultado = num1 * num2
    print("Resultado: ",resultado)
if operacion == '/':
    if num2 == 0:
            print("No existe divison entre cero")
    else:
            resultado = num1 / num2
            print(" Resultado: ",resultado)
