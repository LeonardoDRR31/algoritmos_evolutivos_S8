# Análisis Comparativo de Representaciones Genéticas

## Introducción

Se evaluaron tres tipos de representaciones para resolver el problema de distribuir 39 alumnos en 3 exámenes (A, B, C) de forma equitativa y balanceada en promedio de notas. Las representaciones son:

- Representación Binaria
- Representación Permutacional
- Representación Real (valores continuos)

---

## Resultados resumidos

| Representación      | Equilibrio en grupos | Desviación estándar entre promedios | Convergencia (generaciones) | Observaciones principales                           |
|--------------------|----------------------|-------------------------------------|-----------------------------|----------------------------------------------------|
| Binaria            | No exacto (12,13,14) | 0.4119                              | Nula mejora en 80 generaciones | Estancamiento, penalización constante, poco eficiente |
| Permutacional      | Exacto (13,13,13)    | 0.0363                              | Mejora constante, ~40 gen    | Muy buena solución, buen balance y diversidad       |
| Real               | Exacto (13,13,13)    | 0.0363                              | Rápida (~30 generaciones)    | Mejor control estadístico, solución más robusta     |

---

## Conclusión Detallada

### Representación Real – La más robusta y precisa

- Usa pesos reales normalizados para asignar alumnos a exámenes.
- Permite flexibilidad y exploración continua del espacio de soluciones.
- Logra equilibrio exacto en número de alumnos y minimiza la desviación entre promedios.
- Controla la varianza interna en los grupos, favoreciendo homogeneidad.
- Converge rápido y evita estancamientos.
- Ideal para problemas donde se busca alta precisión y control.

### Representación Permutacional – Eficiente y equilibrada

- Cromosoma representa una permutación de alumnos asignados en secuencia.
- Mantiene equilibrio exacto en tamaño de grupos.
- Ofrece desviación estándar baja, comparable a la representación real.
- Puede incluir incentivos para diversidad interna.
- Mejora progresivamente el fitness.
- Simple de implementar y eficiente para problemas de partición.

### Representación Binaria – Ineficiente para este problema

- Representa asignaciones explícitas con bits.
- No mantiene equilibrio automático, causando penalizaciones por tamaños desiguales.
- No mostró mejora en fitness durante las generaciones evaluadas.
- Sensible a mutaciones aleatorias, exploración poco efectiva.
- Requiere restricciones adicionales para equilibrar grupos, aumentando complejidad.

---

## Recomendaciones

- **Usar representación real** para obtener soluciones precisas y controladas estadísticamente.
- **Usar representación permutacional** para un enfoque sencillo y eficiente cuando el orden y equilibrio son importantes.
- Evitar la representación binaria a menos que se implementen mecanismos complejos para mantener el equilibrio.

---

## Referencias

- Implementaciones y resultados basados en el problema de distribución de alumnos para exámenes usando algoritmos genéticos.
