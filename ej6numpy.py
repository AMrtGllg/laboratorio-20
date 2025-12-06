import numpy as np

def normalizar_np(lista, modo):
    arr = np.array(lista, dtype=float)

    if modo == "minmax":
        minimo = arr.min()
        maximo = arr.max()
        rango = maximo - minimo
        if rango == 0:
            return np.zeros_like(arr)
        return (arr - minimo) / rango

    elif modo == "zscore":
        media = arr.mean()
        desvio = arr.std()
        if desvio == 0:
            return np.zeros_like(arr)
        return (arr - media) / desvio

    elif modo == "unit":
        norma = np.linalg.norm(arr)
        if norma == 0:
            return np.zeros_like(arr)
        return arr / norma

    else:
        raise ValueError("Modo inválido")

valores = [10, 20, 30]

print("Datos originales:", valores)

print("\nMinMax (0 a 1):")
print("Cada valor se escala entre mínimo y máximo del vector.")
print(normalizar_np(valores, "minmax"))

print("\nZ-score:")
print("Cada valor se centra en la media y se divide por la desviación estándar.")
print(normalizar_np(valores, "zscore"))

print("\nUnit norm:")
print("El vector completo se escala para que su longitud (norma) sea 1.")
print(normalizar_np(valores, "unit"))
