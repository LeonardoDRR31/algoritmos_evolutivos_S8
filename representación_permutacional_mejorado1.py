import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Carga de datos ---
df = pd.read_csv('notas_1u.csv')
alumnos = df['Alumno'].tolist()
notas = df['Nota'].tolist()

# --- Cambios para 4 exámenes ---
N_ALUMNOS = 39
N_EXAMENES = 4
TAM_GRUPO = N_ALUMNOS // N_EXAMENES  # 9 (porque 39/4=9.75)

# Para repartir los 39 alumnos en 4 grupos, hacemos 3 grupos de 10 y 1 de 9 o viceversa.
# Por simplicidad, hacemos grupos: 10,10,10,9
GRUPOS = [10,10,10,9]
EXAMENES = ['A','B','C','D']

def crear_cromosoma():
    indices = list(range(N_ALUMNOS))
    random.shuffle(indices)
    return indices

def decodificar_cromosoma(cromosoma):
    asignaciones = {}
    start = 0
    for i, ex in enumerate(EXAMENES):
        end = start + GRUPOS[i]
        asignaciones[ex] = cromosoma[start:end]
        start = end
    return asignaciones

def calcular_fitness(cromosoma):
    asignaciones = decodificar_cromosoma(cromosoma)
    
    promedios = {}
    for examen in EXAMENES:
        indices = asignaciones[examen]
        notas_examen = [notas[i] for i in indices]
        promedios[examen] = np.mean(notas_examen)
    
    desv_promedios = np.std(list(promedios.values()))

    # Penalización si todos los alumnos con nota < 11 están en un mismo examen
    indices_bajos = [i for i, nota in enumerate(notas) if nota < 11]
    examen_con_bajos = {ex: 0 for ex in EXAMENES}
    for i in indices_bajos:
        for examen in EXAMENES:
            if i in asignaciones[examen]:
                examen_con_bajos[examen] += 1

    max_bajos_en_examen = max(examen_con_bajos.values())
    penalizacion = 0
    if max_bajos_en_examen == len(indices_bajos):  # Todos están en el mismo grupo
        penalizacion = 2.0

    # Bonus por diversidad de notas
    bonus_diversidad = 0
    for examen in EXAMENES:
        notas_examen = [notas[i] for i in asignaciones[examen]]
        if max(notas_examen) - min(notas_examen) > 5:
            bonus_diversidad += 0.1

    fitness = -desv_promedios + bonus_diversidad - penalizacion
    return fitness

def mutacion_intercambio(cromosoma):
    cromosoma_mutado = cromosoma.copy()
    if random.random() < 0.3:
        pos1 = random.randint(0, N_ALUMNOS-1)
        pos2 = random.randint(0, N_ALUMNOS-1)
        cromosoma_mutado[pos1], cromosoma_mutado[pos2] = cromosoma_mutado[pos2], cromosoma_mutado[pos1]
    return cromosoma_mutado

def mutacion_inversion(cromosoma):
    cromosoma_mutado = cromosoma.copy()
    if random.random() < 0.2:
        inicio = random.randint(0, N_ALUMNOS - 5)
        longitud = random.randint(2, 5)
        segmento = cromosoma_mutado[inicio:inicio + longitud]
        segmento.reverse()
        cromosoma_mutado[inicio:inicio + longitud] = segmento
    return cromosoma_mutado

def algoritmo_genetico(generaciones=50, tam_poblacion=30):
    poblacion = [crear_cromosoma() for _ in range(tam_poblacion)]
    historial_fitness = []
    
    for gen in range(generaciones):
        fitness_scores = [(crom, calcular_fitness(crom)) for crom in poblacion]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        historial_fitness.append(fitness_scores[0][1])
        
        nueva_poblacion = []
        elite = int(tam_poblacion * 0.2)
        for i in range(elite):
            nueva_poblacion.append(fitness_scores[i][0])
        
        while len(nueva_poblacion) < tam_poblacion:
            padre1 = random.choice(poblacion[:tam_poblacion//3])
            padre2 = random.choice(poblacion[:tam_poblacion//3])
            hijo = mutacion_intercambio(padre1)
            hijo = mutacion_inversion(hijo)
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
        
        if gen % 10 == 0:
            print(f"Generación {gen}: Mejor fitness = {fitness_scores[0][1]:.4f}")
    
    mejor_cromosoma = fitness_scores[0][0]
    return mejor_cromosoma, historial_fitness

print("REPRESENTACIÓN PERMUTACIONAL")
print("Problema: Secuenciar alumnos para asignación ordenada a 4 exámenes")
print(f"Cromosoma: Permutación de {N_ALUMNOS} índices de alumnos")
print(f"Decodificación: Grupos según tamaños {GRUPOS} para exámenes {EXAMENES}\n")

mejor_solucion, historial = algoritmo_genetico()
asignaciones_finales = decodificar_cromosoma(mejor_solucion)

print("\nAsignación final por orden de secuencia:")
for examen in EXAMENES:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedio = np.mean(notas_examen)
    print(f"\nExamen {examen}: {len(indices)} alumnos, promedio = {promedio:.2f}")
    print(f"  Secuencia de alumnos:")
    for i, idx in enumerate(indices):
        print(f"    Posición {i+1}: {alumnos[idx]} (Nota: {notas[idx]})")
        if i >= 4:
            print("    ... (mostrando primeros 5)")
            break

print("\nEstadísticas finales:")
promedios = []
rangos = []
for examen in EXAMENES:
    indices = asignaciones_finales[examen]
    notas_examen = [notas[i] for i in indices]
    promedios.append(np.mean(notas_examen))
    rangos.append(max(notas_examen) - min(notas_examen))

print(f"Promedios: " + ", ".join([f"{ex}={prom:.2f}" for ex, prom in zip(EXAMENES, promedios)]))
print(f"Rangos de notas: " + ", ".join([f"{ex}={ran:.0f}" for ex, ran in zip(EXAMENES, rangos)]))
print(f"Desviación estándar entre promedios: {np.std(promedios):.4f}")

print("\nEvolución del algoritmo:")
print(f"Fitness inicial: {historial[0]:.4f}")
print(f"Fitness final: {historial[-1]:.4f}")
print(f"Mejora total: {((historial[-1] - historial[0]) / abs(historial[0]) * 100):.1f}%")

# --- Visualización ---

# Preparar DataFrame para gráficos
datos = []
for examen, indices in asignaciones_finales.items():
    for i in indices:
        datos.append({'Examen': examen, 'Alumno': alumnos[i], 'Nota': notas[i]})
df_notas = pd.DataFrame(datos)

# Evolución fitness
plt.figure(figsize=(10,4))
plt.plot(historial, marker='o')
plt.title('Evolución del fitness por generación')
plt.xlabel('Generación')
plt.ylabel('Fitness')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma notas por examen
plt.figure(figsize=(10,4))
sns.boxplot(x='Examen', y='Nota', hue='Examen', data=df_notas, palette='Set2', dodge=False)
plt.title('Histograma de notas por examen')
plt.xlabel('Nota')
plt.ylabel('Cantidad de alumnos')
plt.tight_layout()
plt.show()

# Boxplot comparación de notas
plt.figure(figsize=(8,5))
sns.boxplot(x='Examen', y='Nota', hue='Examen', data=df_notas, palette='Set2', dodge=False)
plt.title('Comparación de distribuciones de notas por examen')
plt.xlabel('Examen')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()
