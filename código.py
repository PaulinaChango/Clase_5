# Sistema completo de gestión de estudiantes

print("================================================")
print("         SISTEMA DE REGISTRO ACADÉMICO")
print("================================================")

# Datos personales
nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
edad = int(input("Ingrese la edad: "))
curso = input("Ingrese el curso: ")
paralelo = input("Ingrese el paralelo: ")

print("\n========== INGRESO DE NOTAS ==========")

# Ingreso de notas
nota1 = float(input("Ingrese la nota del Primer Parcial: "))
nota2 = float(input("Ingrese la nota del Segundo Parcial: "))
nota3 = float(input("Ingrese la nota del Proyecto Final: "))
nota4 = float(input("Ingrese la nota del Examen Final: "))

# Cálculo del promedio
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Nota mayor y menor
nota_mayor = max(nota1, nota2, nota3, nota4)
nota_menor = min(nota1, nota2, nota3, nota4)

# Asistencia
print("\n========== ASISTENCIA ==========")
asistencia = int(input("Ingrese el porcentaje de asistencia: "))

# Conducta
print("\n========== CONDUCTA ==========")
conducta = input("Ingrese la conducta del estudiante (Excelente/Buena/Regular/Mala): ")

# Reporte general
print("\n================================================")
print("              REPORTE ACADÉMICO")
print("================================================")

print("Nombre completo:", nombre, apellido)
print("Edad:", edad)
print("Curso:", curso)
print("Paralelo:", paralelo)

print("\n========== NOTAS ==========")
print("Primer Parcial:", nota1)
print("Segundo Parcial:", nota2)
print("Proyecto Final:", nota3)
print("Examen Final:", nota4)

print("\nPromedio Final:", round(promedio, 2))
print("Nota más alta:", nota_mayor)
print("Nota más baja:", nota_menor)

# Estado académico
print("\n========== RESULTADO ==========")

if promedio >= 9:
    estado = "Excelente"
elif promedio >= 7:
    estado = "Aprobado"
elif promedio >= 5:
    estado = "Supletorio"
else:
    estado = "Reprobado"

print("Estado académico:", estado)

# Verificación de asistencia
if asistencia >= 75:
    print("Asistencia: Cumple con el mínimo requerido")
else:
    print("Asistencia: No cumple con el mínimo requerido")

# Evaluación de conducta
if conducta.lower() == "excelente":
    print("Conducta destacada")
elif conducta.lower() == "buena":
    print("Conducta adecuada")
elif conducta.lower() == "regular":
    print("Debe mejorar su comportamiento")
else:
    print("Conducta inadecuada")

# Observaciones automáticas
print("\n========== OBSERVACIONES ==========")

if promedio >= 9 and asistencia >= 90:
    print("El estudiante puede recibir reconocimiento académico.")
elif promedio < 7:
    print("El estudiante necesita reforzar conocimientos.")
else:
    print("El estudiante mantiene un rendimiento aceptable.")

# Cálculo de puntos adicionales
participacion = float(input("\nIngrese puntos de participación extra: "))
promedio_final = promedio + participacion

if promedio_final > 10:
    promedio_final = 10

print("\nPromedio con participación:", round(promedio_final, 2))

# Resultado final actualizado
if promedio_final >= 7:
    print("Resultado final: APROBADO")
else:
    print("Resultado final: REPROBADO")

print("\n================================================")
print("        FIN DEL REPORTE DEL ESTUDIANTE")
print("================================================")
print("Gracias por utilizar el sistema académico")