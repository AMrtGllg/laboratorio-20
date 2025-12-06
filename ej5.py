while True:
  n = int(input("Ingrese un número N mayor igual a 3: "))
  if n >= 3:
    break
  print("N debe ser mayor o igual a 3.")

matriz = [[0] * n for _ in range(n)]

num = 1
izq, der = 0, n - 1
arr, aba = 0, n - 1

while izq <= der and arr <= aba:
  for j in range(izq, der + 1):
    matriz[arr][j] = num
    num += 1
  arr += 1

  for i in range(arr, aba + 1):
    matriz[i][der] = num
    num += 1
  der -= 1

  if arr <= aba:
    for j in range(der, izq - 1, -1):
      matriz[aba][j] = num
      num += 1
    aba -= 1

  if izq <= der:
    for i in range(aba, arr - 1, -1):
      matriz[i][izq] = num
      num += 1
    izq += 1

print("\n Matriz espiral")
for fila in matriz:
  print(fila)
print()
