# Sistema de calificaciones con arreglos
# Escribe tu nombre en la línea de abajo.
calificaciones = [85, 67, 92, 74, 58]

print("=== SISTEMA DE CALIFICACIONES ===")
print("Calificaciones iniciales:", calificaciones)
print("\nPrimera calificación (índice 0):", calificaciones[0])
print("Tercera calificación (índice 2):", calificaciones[2])

aprobados = 0
reprobados = 0
print("\nCalificaciones y estado:")
for indice, nota in enumerate(calificaciones):
    if nota >= 70:
        estado = "Aprobado"
        aprobados += 1
    else:
        estado = "Reprobado"
        reprobados += 1
    print(f"Estudiante {indice + 1}: {nota} - {estado}")

promedio = sum(calificaciones) / len(calificaciones)
print(f"\nPromedio del grupo: {promedio:.2f}")
print("Calificación más alta:", max(calificaciones))
print("Calificación más baja:", min(calificaciones))
print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", reprobados)

print("\nVamos a modificar la primera calificación.")
try:
    nueva_nota = float(input("Escribe una nueva nota entre 0 y 100: "))
    if 0 <= nueva_nota <= 100:
        calificaciones[0] = nueva_nota
        print("Vector actualizado:", calificaciones)
        print(f"Nuevo promedio: {sum(calificaciones) / len(calificaciones):.2f}")
    else:
        print("Nota fuera de rango. No se realizó la modificación.")
except ValueError:
    print("Dato no válido. Debes escribir un número.")

print("\nPrograma finalizado.")
