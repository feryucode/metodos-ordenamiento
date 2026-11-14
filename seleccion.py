def ordenamiento_seleccion(tiempos):
    n = len(tiempos)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if tiempos[j] < tiempos[indice_minimo]:
                indice_minimo = j
        tiempos[i], tiempos[indice_minimo] = tiempos[indice_minimo], tiempos[i]
    return tiempos

tiempos_carrera = [14.2, 11.8, 13.5, 10.9, 12.4, 15.1, 11.2]
print("Tiempos originales (s):", tiempos_carrera)
tiempos_ordenados = ordenamiento_seleccion(tiempos_carrera)
print("Tiempos ordenados (s):", tiempos_ordenados)