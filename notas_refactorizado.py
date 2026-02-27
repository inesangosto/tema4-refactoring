def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def obtener_aprobado(media):
    return media >= 5

def obtener_calificacion(media):
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

def mostrar_informe_alumno(nombre_alumno, nota1, nota2, nota3):  
    media = calcular_media(nota1, nota2, nota3)
    estado = obtener_aprobado(media)
    calificacion = obtener_calificacion(media)

    print(f"Alumno: {nombre_alumno}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Media: {media}")
    print(f"Resultado: {'Aprobado' if estado else 'Suspendido'}")
    print(f"Calificación: {calificacion}")
    print("----------------------")


def main():
    mostrar_informe_alumno("Ana García", 8, 7, 9)
    mostrar_informe_alumno("Luis Pérez", 4, 5, 3)
    mostrar_informe_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()