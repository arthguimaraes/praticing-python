def somar(a, b):
    return a + b

print("---------------")
print("SOMA DE VALORES")
print("---------------\n")

try:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
except ValueError:
    print("Digite valores válidos! Tente novamente.")
    
resultado = somar(numero1, numero2)
print(f"O resultado da soma é: {resultado}")

