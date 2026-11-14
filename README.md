# Métodos de Ordenamiento en Python

Este repositorio contiene la implementación práctica de tres algoritmos clásicos de ordenamiento desarrollados en Python. Cada script resuelve un caso de uso distinto ordenando colecciones de datos de forma ascendente sin utilizar funciones nativas del lenguaje como `sort()` o `sorted()`.

## Contenido del Repositorio y Ejercicios

### 1. Método de la Burbuja (Bubble Sort)
* **Archivo:** `burbuja.py`
* **Planteamiento del ejercicio:** Un profesor necesita ordenar las calificaciones finales de un grupo de estudiantes de menor a mayor para identificar rápidamente el rango de aprovechamiento del salón.
* **Lógica aplicada:** El algoritmo recorre la lista de calificaciones comparando pares de elementos adyacentes. Si la calificación actual es mayor que la siguiente, ambas intercambian su posición. Este proceso se repite en múltiples pasadas hasta que las calificaciones más altas suben hacia el final de la lista.
* **Datos de entrada:** `[85, 70, 95, 60, 88, 76, 100, 65]`
* **Salida en consola:**
  * `Calificaciones originales: [85, 70, 95, 60, 88, 76, 100, 65]`
  * `Calificaciones ordenadas: [60, 65, 70, 76, 85, 88, 95, 100]`

### 2. Método por Inserción (Insertion Sort)
* **Archivo:** `insercion.py`
* **Planteamiento del ejercicio:** El sistema de inventario de una tienda requiere ordenar los precios de diversos artículos con valores decimales desde el más económico hasta el más caro para mostrarlos en su catálogo.
* **Lógica aplicada:** El algoritmo toma un precio a la vez empezando desde el segundo elemento y lo compara con los precios que están a su izquierda, desplazando hacia la derecha los valores mayores hasta encontrar la posición exacta donde debe insertarse.
* **Datos de entrada:** `[250.50, 120.00, 89.99, 450.00, 15.75, 310.20]`
* **Salida en consola:**
  * `Precios originales: [250.5, 120.0, 89.99, 450.0, 15.75, 310.2]`
  * `Precios ordenados: [15.75, 89.99, 120.0, 250.5, 310.2, 450.0]`

### 3. Método por Selección (Selection Sort)
* **Archivo:** `seleccion.py`
* **Planteamiento del ejercicio:** En una competencia de atletismo de 100 metros planos, se registraron los tiempos en segundos de los corredores. Se necesita ordenar los registros del tiempo más bajo (el corredor más rápido) al más alto (el más lento) para definir las posiciones finales.
* **Lógica aplicada:** El algoritmo divide la lista en una parte ordenada y otra desordenada. En cada iteración, busca el tiempo más bajo dentro de la sección desordenada, guarda su índice y lo intercambia directamente con el primer elemento de dicha sección.
* **Datos de entrada:** `[12.4, 10.8, 11.5, 13.1, 10.2, 11.9]`
* **Salida en consola:**
  * `Tiempos originales (s): [12.4, 10.8, 11.5, 13.1, 10.2, 11.9]`
  * `Tiempos ordenados (s): [10.2, 10.8, 11.5, 11.9, 12.4, 13.1]`

## Comparativa de Complejidad

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso | Complejidad Espacial |
| :--- | :---: | :---: | :---: | :---: |
| **Burbuja** | O(n) | O(n²) | O(n²) | O(1) |
| **Inserción** | O(n) | O(n²) | O(n²) | O(1) |
| **Selección** | O(n²) | O(n²) | O(n²) | O(1) |

