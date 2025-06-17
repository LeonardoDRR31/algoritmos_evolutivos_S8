# Análisis Comparativo de Representaciones para Distribución de Alumnos

---

## Representación Binaria

- **Problema:** Distribuir 39 alumnos en 3 exámenes (A, B, C) de forma equitativa  
- **Cromosoma:** 117 bits (39 alumnos × 3 bits cada uno)  
- **Gen ejemplo:** `[0,1,0]` significa alumno asignado a examen B  

### Evolución del fitness:
| Generación | Mejor fitness  |
|------------|---------------|
| 0          | -1000.0000    |
| 20         | -1000.0000    |
| 40         | -1000.0000    |
| 60         | -1000.0000    |
| 80         | -1000.0000    |

### Distribución final:
| Examen | Alumnos | Promedio |
|--------|---------|----------|
| A      | 13      | 15.92    |
| B      | 12      | 14.92    |
| C      | 14      | 15.36    |

- **Verificación de equilibrio:**  
  Desviación estándar entre promedios: **0.4119**

---

## Representación Permutacional

- **Problema:** Secuenciar alumnos para asignación ordenada a exámenes  
- **Cromosoma:** Permutación de 39 índices de alumnos  
- **Decodificación:** Posiciones [0-12] → Examen A, [13-25] → Examen B, [26-38] → Examen C  

### Evolución del fitness:
| Generación | Mejor fitness |
|------------|--------------|
| 0          | 0.2275       |
| 10         | 0.2275       |
| 20         | 0.2637       |
| 30         | 0.2637       |
| 40         | 0.2637       |

### Distribución final:
| Examen | Alumnos | Promedio |
|--------|---------|----------|
| A      | 13      | 15.38    |
| B      | 13      | 15.46    |
| C      | 13      | 15.38    |

- **Desviación estándar entre promedios:** **0.0363**  
- **Mejora total del fitness:** 15.9% (de 0.2275 a 0.2637)

---

## Representación Real

- **Problema:** Optimizar distribución de alumnos usando pesos probabilísticos  
- **Cromosoma:** 117 valores reales (39 alumnos × 3 pesos normalizados)  
- **Gen ejemplo:** `[0.2, 0.5, 0.3]` representa probabilidades para exámenes A, B, C  

### Evolución del fitness:
| Generación | Mejor fitness |
|------------|--------------|
| 0          | -1.1840      |
| 30         | -1.0911      |
| 60         | -1.0911      |
| 90         | -1.0911      |
| 120        | -1.0911      |

### Distribución optimizada:
| Examen | Alumnos | Promedio | Varianza | Rango de notas |
|--------|---------|----------|----------|----------------|
| A      | 13      | 15.38    | 9.47     | [11 - 20]      |
| B      | 13      | 15.46    | 12.71    | [9 - 20]       |
| C      | 13      | 15.38    | 9.47     | [10 - 20]      |

- **Desviación estándar entre promedios:** **0.0363**  
- **Diferencia máxima entre promedios:** 0.08

---

## Conclusión

- La **representación permutacional** y la **representación real** logran un equilibrio mucho mejor entre los grupos, reflejado en una desviación estándar entre promedios muy baja (**0.0363**) en comparación con la representación binaria (**0.4119**).  
- La representación binaria muestra poca evolución en el fitness a lo largo de las generaciones, permaneciendo constante en un valor muy bajo (-1000), lo que indica dificultades para encontrar una buena solución.  
- La representación permutacional converge más rápido y muestra una mejora notable (15.9%) en el fitness en menos generaciones (20-40 generaciones).  
- La representación real proporciona una solución robusta y probabilística, con una buena distribución de varianzas y rangos de notas, aunque su mejora en fitness es más lenta y se estabiliza después de 30 generaciones.  
- En términos prácticos, la representación permutacional ofrece una mejor relación entre calidad de solución y velocidad de convergencia, mientras que la representación real permite modelar la incertidumbre y puede ser más flexible en casos más complejos.

---

Si quieres puedo ayudarte también a crear un README.md o agregar instrucciones para que tu repo quede impecable. ¿Quieres?
