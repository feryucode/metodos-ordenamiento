# Métodos de Ordenamiento en Python

Este repositorio contiene la implementación práctica de tres algoritmos clásicos de ordenamiento desarrollados en Python. Cada script resuelve un caso de uso distinto ordenando colecciones de datos de forma ascendente sin utilizar funciones nativas del lenguaje (como `sort()` o `sorted()`).

---

## Contenido del Repositorio y Ejercicios

### 1. Método de la Burbuja (Bubble Sort)
* **Planteamiento del ejercicio:** Un profesor necesita ordenar las calificaciones finales de un grupo de estudiantes de menor a mayor para identificar rápidamente el rango de aprovechamiento del salón.
* **Lógica aplicada:** El algoritmo recorre la lista de calificaciones comparando pares de elementos adyacentes. Si la calificación actual es mayor que la siguiente, ambas intercambian su posición. Este proceso se repite en múltiples pasadas hasta que las calificaciones más altas "burbujean" hacia el final de la lista.
* **Datos de entrada:** `[85, 70, 95, 60, 88, 76, 100, 65]`
* **Salida esperada:**
  ```text
  Calificaciones originales: [85, 70, 95, 60, 88, 76, 100, 65]
  Calificaciones ordenadas: [60, 65, 70, 76, 85, 88, 95, 100]
