ingreso_mensual=float(input("Ingreso mensual:"))
ingreso_anual= ingreso_mensual *14

print("Calculadora de impuestos")
print("Ingreso anual", ingreso_anual)

restante= ingreso_anual
impuesto_total=0.0

tramo= min(restante, 20000)
impuesto_tramo1= tramo *0.0
impuesto_total+=impuesto_tramo1
restante-=tramo
print("Tramo 1 (0-20000):", impuesto_tramo1)

if restante > 0:
    tramo= min(restante, 30000)
    impuesto_tramo2= tramo *0.1
    impuesto_total+=impuesto_tramo2
    restante-=tramo
    print("Tramo 2 (20000-50000):", impuesto_tramo2)

if restante > 0:
    tramo= min(restante, 50000)
    impuesto_tramo3= tramo *0.2
    impuesto_total+=impuesto_tramo3
    restante-=tramo
    print("Tramo 3 (50000-100000):", impuesto_tramo3)

if restante > 0:
    impuesto_tramo4= tramo *0.3
    impuesto_total+=impuesto_tramo4
    restante-=tramo
    print("Tramo 4 (Mayor a 100000):", impuesto_tramo4)

tasa_efectiva= (impuesto_total/ingreso_anual)*100 if ingreso_anual>0 else 0

print("Impuesto total: ", impuesto_total)
print("Tasa efectiva (%): ", tasa_efectiva)
print()