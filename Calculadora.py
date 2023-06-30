print("Bienvenido a esta calculadora")
print("------------------------------")
print()
x = int(input("Dijite el primer numero: "))
print()
y = int(input("Dijite el segundo numer: "))
print()
op = input("Dijite la operacion: ")
print()

if op == "suma":
    result = x + y
    print(f"el resultado es : {result}")
elif op == "resta":
    result = x - y
    print(f"el resultado es : {result}")
elif op == "multiplicacion":
    result = x * y
    print(f"el resultado es : {result}")
elif op == "divsion":
    result = x / y
    print(f"el resultado es : {result}")
