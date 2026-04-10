import matplotlib.pyplot as plt

def calcular_collatz(n):
    """Calcula la cantidad de iteraciones para que n converja a 1."""
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

# --- Lógica Principal ---

# 1. Definir rangos
limite_superior = 10000
numeros_n = list(range(1, limite_superior + 1))
conteo_iteraciones = []

# 2. Procesar cada número
for n in numeros_n:
    resultado = calcular_collatz(n)
    conteo_iteraciones.append(resultado)

# 3. Configuración del Gráfico
plt.figure(figsize=(12, 6))

# Eje X: Número n de comienzo
# Eje Y: Número de iteraciones
plt.scatter(numeros_n, conteo_iteraciones, s=1, alpha=0.5, color='blue')

plt.title('Conjetura de Collatz (1 a 10.000)')
plt.xlabel('Número de inicio (n)')
plt.ylabel('Número de iteraciones para converger')
plt.grid(True, linestyle='--', alpha=0.7)

# 4. Mostrar y/o guardar el gráfico
print("Generando gráfico...")
plt.show()