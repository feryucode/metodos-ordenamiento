def ordenamiento_burbuja(calificaciones):
    n = len(calificaciones)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if calificaciones[j] > calificaciones[j + 1]:
                calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]
    return calificaciones

notas_estudiantes = [85, 70, 95, 60, 88, 76, 100, 65]
print("Calificaciones originales:", notas_estudiantes)
notas_ordenadas = ordenamiento_burbuja(notas_estudiantes)
print("Calificaciones ordenadas:", notas_ordenadas)