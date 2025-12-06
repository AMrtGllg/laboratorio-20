def normalizar(lista, modo):
  datos = list(lista)

  if modo == "minmax":
    minimo = min(datos)
    maximo = max(datos)
    rango = maximo - minimo
    if rango == 0:
      return [0.0 for _ in datos]
    return [(x - minimo) / rango for x in datos]

  elif modo == "zscore":
    media = sum(datos) / len(datos)
    var = sum((x - media) ** 2 for x in datos) / len(datos)
    desvio = var ** 0.5
    if desvio == 0:
      return [0.0 for _ in datos]
    return [(x - media) / desvio for x in datos]

  elif modo == "unit":
    norma = sum(x ** 2 for x in datos) ** 0.5
    if norma == 0:
      return [0.0 for _ in datos]
    return [x / norma for x in datos]

  else:
    raise ValueError("Modo inválido: " + str(modo))


valores = [10, 20, 30]

print("Datos originales:", valores)

print("\nMinMax (0 a 1):")
print("Cada valor se escala entre mínimo y máximo del vector.")
print(normalizar(valores, "minmax"))

print("\nZ-score:")
print("Cada valor se centra en la media y se divide por la desviación estándar.")
print(normalizar(valores, "zscore"))

print("\nUnit norm:")
print("El vector completo se escala para que su longitud (norma) sea 1.")
print(normalizar(valores, "unit"))
