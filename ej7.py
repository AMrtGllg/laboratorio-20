# ej7
estudiantes = []

def agregar_estudiante():
  nombre = input("Nombre: ")
  edad = int(input("Edad: "))
  promedio = float(input("Promedio: "))
  estudiante = {"nombre": nombre, "edad": edad, "promedio": promedio}
  estudiantes.append(estudiante)
  print("Estudiante agregado.\n")

def mostrar_estudiantes():
  if not estudiantes:
    print("No hay estudiantes.\n")
    return
  for e in estudiantes:
    print(e)
  print()

def mostrar_mejor_promedio():
  if not estudiantes:
    print("No hay estudiantes.\n")
    return
  mejor = max(estudiantes, key=lambda e: e["promedio"])
  print("Mejor promedio:", mejor, "\n")

def buscar_por_nombre():
  nombre = input("Nombre a buscar: ")
  encontrados = [e for e in estudiantes if e["nombre"] == nombre]
  if encontrados:
    for e in encontrados:
      print(e)
  else:
    print("No encontrado\n")

if __name__ == "__main__":
  print(">>> MENÚ EJ7 <<<")
  while True:
    print("1) Agregar  2) Mostrar  3) Mejor promedio  4) Buscar  0) Salir")
    op = input("Opción: ")
    if op == "1":
      agregar_estudiante()
    elif op == "2":
      mostrar_estudiantes()
    elif op == "3":
      mostrar_mejor_promedio()
    elif op == "4":
      buscar_por_nombre()
    elif op == "0":
      break
    else:
      print("Opción inválida\n")
