# Actividad 4: Restricciones Adicionales

## Representación Permutacional

- **Problema:** Asignar 39 alumnos a 3 exámenes (A, B, C) de forma equilibrada.
- **Cromosoma:** Permutación de los índices de alumnos.
- **Decodificación:** Posiciones [0–12] → A, [13–25] → B, [26–38] → C.
- **Restricción agregada:** Los alumnos con **nota < 11** no pueden estar todos en el mismo examen.

---

## Resultados con restricción aplicada

| Examen | Nº de Alumnos | Promedio | Rango de Notas | Alumnos con Nota < 11 |
|--------|----------------|----------|----------------|----------------------|
| A      | 13             | 15.38    | 8              | ✅ Distribuidos      |
| B      | 13             | 15.38    | 11             | ✅ Distribuidos      |
| C      | 13             | 15.46    | 11             | ✅ Distribuidos      |

- **Desviación estándar entre promedios:** `0.0363`
- **Fitness inicial:** `0.1081`
- **Fitness final:** `0.2637`
- **Mejora total:** `+143.9%`

---

## Interpretación

- La distribución final **cumple con la restricción**, ya que los alumnos con notas menores a 11 están repartidos entre varios exámenes.
- El algoritmo logró mejorar significativamente el fitness, mostrando una buena adaptación al nuevo criterio.
- La desviación entre promedios es muy baja, lo que sugiere un excelente equilibrio.
- Los rangos de notas en cada examen indican una buena **diversidad interna**.

---

## Conclusión

La inclusión de la restricción que prohíbe agrupar a todos los alumnos con bajo rendimiento en un solo examen fue correctamente incorporada en la función de `fitness`. El algoritmo no solo respetó esta condición, sino que también mejoró el rendimiento general, manteniendo un balance en los promedios y la diversidad entre grupos. Esta modificación demuestra que las restricciones específicas pueden integrarse eficazmente sin comprometer la eficiencia del algoritmo genético.

