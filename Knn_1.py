import math

# Leer archivo CSV
with open('iris.csv', 'r', encoding='utf-8-sig') as f:
    dataframe = [line.strip().split(',') for line in f]

# Convertir valores a flotantes
for row in dataframe:
    for i in range(4):
        row[i] = float(row[i])

# Definir instancia de prueba
caso = [4.9,3.1,1.5,0.1] #sentosa

# Calcular distancia euclidiana entre instancia de prueba y cada instancia de datos
distances = []
for row in dataframe:
    dist = math.sqrt(sum([(row[i] - caso[i])**2 for i in range(4)]))
    distances.append((dist, row[4]))

# Ordenar distancias de menor a mayor
distances.sort()

# Seleccionar las k instancias más cercanas
k = 3
k_nearest = [d[1] for d in distances[:k]]

# Hacer una predicción basada en las clases de las k instancias más cercanas
prediction = max(set(k_nearest), key=k_nearest.count)

# Imprimir la predicción

print("La predicción es:", prediction)
