# 🧬 Actividad 2: Modificación de Fitness – Representación Binaria

## 📋 Comparación de Resultados

| Aspecto                            | Versión Original               | Versión Modificada              |
|-----------------------------------|-------------------------------|-----------------------------------|
| **Fitness inicial**               | -1000.0000                    | 59.3728                           |
| **Fitness final**                 | -1000.0000                    | 74.9941                           |
| **Mejora de fitness**             | ❌ Ninguna                    | ✅ +15.62 puntos                  |
| **Promedio Examen A**             | 15.92                         | 15.46                             |
| **Promedio Examen B**             | 14.92                         | 18.31                             |
| **Promedio Examen C**             | 15.36                         | 12.46                             |
| **Desv. estándar entre promedios**| 0.4119                        | 2.3870                            |
| **Evolución observable**          | ❌ Estancado desde el inicio | ✅ Mejora gradual por generaciones |

---

## 🧠 Interpretación

- La función original usaba una penalización extrema (-1000) cuando los grupos no tenían exactamente 13 alumnos, lo que impedía cualquier progreso en la búsqueda.
- La nueva función:
  - **Permite la evolución** del algoritmo mediante un sistema de penalizaciones más progresivo.
  - **Premia la diversidad interna** dentro de cada examen (variedad en los niveles de notas).
  - **Penaliza la varianza alta** en los grupos, lo que en teoría promueve homogeneidad.

### ⚠️ Sin embargo:
- El nuevo fitness prioriza **diversidad dentro de los grupos** más que **equilibrio global entre los exámenes**.
- Esto generó **una gran brecha** entre los promedios de los exámenes, con diferencias superiores a 5 puntos.

---

## ✅ Conclusión

La modificación en la función de fitness permitió que el algoritmo **saliera del estancamiento** y encontrara soluciones válidas con mejor adaptación. Sin embargo, al **no equilibrar adecuadamente la penalización entre diversidad y equidad entre grupos**, se sacrificó el objetivo principal de **igualar los promedios de los exámenes**.

### 🛠️ Recomendaciones:
- Ajustar los **pesos** entre las penalizaciones para dar mayor importancia a la equidad de promedios.
- Incluir un límite de tolerancia en la diferencia máxima permitida entre los promedios (e.g., no más de 1.0).

---
