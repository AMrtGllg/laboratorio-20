salario_base=2000
horas_extras=20
pago_hora_extra=100
bono=100
afp=12
salud=30
salario_bruto=salario_base+(horas_extras*pago_hora_extra)+bono
descuentos_totales=(salario_base * afp/100)+(salario_base * salud/100)

salario_neto = salario_base + (horas_extras * pago_hora_extra) + bono - descuentos_totales
print("Salario bruto:", salario_bruto)
print("Descuentos totales:", descuentos_totales)
print("Salario neto:", salario_neto)
print()