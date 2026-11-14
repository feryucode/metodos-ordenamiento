def ordenamiento_insercion(precios):
    for i in range(1, len(precios)):
        actual = precios[i]
        j = i - 1
        while j >= 0 and actual < precios[j]:
            precios[j + 1] = precios[j]
            j -= 1
        precios[j + 1] = actual
    return precios

precios_inventario = [250.50, 120.00, 45.99, 310.25, 89.90, 15.00]
print("Precios originales:", precios_inventario)
precios_ordenados = ordenamiento_insercion(precios_inventario)
print("Precios ordenados:", precios_ordenados)