# Actividad 3: Comparación del Operador de Mutación Gaussiana

## Tabla Comparativa

| Sigma (σ) | Fitness Final | Promedios A/B/C        | Desv. Est. Promedios | Varianzas A/B/C      | Diferencia Máx. Promedios |
|-----------|----------------|-----------------------|----------------------|----------------------|---------------------------|
| 0.01      | -1.0911        | 15.38 / 15.46 / 15.38 | 0.0363               | 9.93 / 12.25 / 9.47  | 0.08                      |
| 0.1       | -1.0911        | 15.38 / 15.46 / 15.38 | 0.0363               | 8.54 / 8.86 / 14.24  | 0.08                      |
| 0.3       | -1.0911        | 15.38 / 15.46 / 15.38 | 0.0363               | 12.54 / 10.86 / 8.24 | 0.08                      |

## Interpretación

- **Fitness final** se estabiliza en `-1.0911` para todos los valores de sigma, lo que sugiere que el algoritmo converge consistentemente hacia una solución similar en cuanto al equilibrio de promedios.
- **Promedios por examen** permanecen casi idénticos en todos los casos, indicando un reparto equitativo.
- **Desviación estándar de los promedios** también es constante (0.0363), señal de equilibrio mantenido en las tres pruebas.
- Sin embargo, **las varianzas dentro de cada grupo** muestran diferencias significativas según `σ`. A menor sigma (0.01), las varianzas son más uniformes. A sigma más alto (0.3), hay una mayor dispersión entre grupos, mostrando que las mutaciones más agresivas generan mayor variabilidad interna.

## Conclusión

El operador de mutación gaussiana con diferentes valores de `σ` afecta principalmente a la **homogeneidad interna de cada grupo** (varianza), pero **no** altera significativamente el equilibrio global en términos de promedios entre grupos.

- Para soluciones más estables y homogéneas dentro de cada grupo, conviene usar **σ bajo (ej. 0.01)**.
- σ más alto como 0.3 puede ser útil si se busca **mayor diversidad genética**, pero con el riesgo de generar asignaciones con mayor desigualdad interna.
