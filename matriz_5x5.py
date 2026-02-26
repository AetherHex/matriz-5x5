"""
matriz = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la fila [{i}] columna [{j}]: "))
        matriz[i][j] = valor

print("\nMATRIZ:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t")
    print()
"""

v = [[0 for _ in range(3)] for _ in range(3)]
print(v)