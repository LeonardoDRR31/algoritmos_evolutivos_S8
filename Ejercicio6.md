# Actividad 6: Problema Extendido – Distribución en 4 Exámenes

## Representación Permutacional

### Problema
Extender el problema de asignación de estudiantes desde 3 exámenes (A, B, C) a 4 exámenes (A, B, C, D), manteniendo la equidad en distribución de notas entre los grupos.

---

## ¿Qué cambios necesitas hacer en el cromosoma?

**Cromosoma original:**  
Una permutación de 39 índices de alumnos, con asignación por posición:
- [0–12] → Examen A
- [13–25] → Examen B
- [26–38] → Examen C

**Cromosoma modificado para 4 exámenes:**
- Se mantiene como una **permutación de 39 índices**, pero cambia la forma de **decodificar**:
  - [0–9]   → Examen A (10 alumnos)
  - [10–19] → Examen B (10 alumnos)
  - [20–29] → Examen C (10 alumnos)
  - [30–38] → Examen D (9 alumnos)

**Resumen de cambios:**
- No se modifica la estructura del cromosoma.
- Se **ajusta la lógica de decodificación** y evaluación (`decodificar_cromosoma` y `calcular_fitness`) para distribuir los índices en 4 grupos en lugar de 3.

---

## ¿Cómo afecta esto a la convergencia del algoritmo?

### Observaciones empíricas:

Al ejecutar múltiples veces el algoritmo con 4 exámenes, se observaron los siguientes comportamientos:

| Ejecución | Fitness inicial | Fitness final | Mejora (%) | Mejor fitness alcanzado    |
|-----------|-----------------|----------------|-------------|--------------------------|
| 1         | 0.0945          | 0.3808         | 303.1%      | Excelente                |
| 2         | 0.1288          | 0.3808         | 195.6%      | Excelente                |
| 3         | 0.1870          | 0.3808         | 103.6%      | Excelente                |

- La **desviación estándar entre promedios** fue consistentemente baja: `~0.0192`, indicando buena convergencia.
- La **mejora del fitness** fue significativa, aunque dependiente del valor inicial.

### Efecto en la convergencia:

1. **Mayor complejidad**:  
   Con 4 grupos en lugar de 3, el número de combinaciones posibles para lograr una distribución balanceada aumenta, lo que puede hacer más difícil alcanzar soluciones óptimas rápidamente.

2. **Convergencia más lenta en algunas ejecuciones**:  
   Se observó que en algunas corridas el fitness se estabiliza durante varias generaciones (plateau), antes de mejorar finalmente.

3. **Mayor presión sobre diversidad**:  
   La distribución justa requiere que la diversidad de notas esté bien repartida entre más grupos, lo cual puede hacer que los operadores genéticos (mutación e inversión) tarden más en producir individuos de alta calidad.

---

## Conclusión

El cambio al problema extendido con 4 exámenes no requiere una modificación en la estructura del cromosoma, solo en su interpretación. Sin embargo, **afecta directamente la convergencia del algoritmo**, al aumentar la complejidad del espacio de búsqueda y la dificultad de balancear más grupos. Aun así, el algoritmo fue capaz de adaptarse eficazmente, logrando buenas soluciones en todas las ejecuciones observadas.
