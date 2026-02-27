# Programa para calcular la nota media, determinar si han aprobado y asignar una calificación.
# Autor: Inés Angosto
# Fecha: 27/02/2026

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media de tres notas.

    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    return (nota1 + nota2 + nota3) / 3  # cálculo de la media


def obtener_aprobado(media):
    """
    Determina si un alumno ha aprobado según su media.

    Args:
        media (float): Media de las notas del alumno.

    Returns:
        bool: True si la media es mayor o igual a 5, False en caso contrario.
    """
    return media >= 5  # aprobado si la media es 5 o más


def obtener_calificacion(media):
    """
    Asigna una calificación según la media del alumno.

    Args:
        media (float): Media de las notas del alumno.

    Returns:
        str: Calificación en texto:
             "Sobresaliente", "Notable", "Aprobado" o "Suspenso".
    """
    if media >= 9:
        return "Sobresaliente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Suspenso"


def mostrar_informe_alumno(nombre_alumno, nota1, nota2, nota3):
    """
    Muestra un informe completo del alumno: notas, media, estado y calificación.

    Args:
        nombre_alumno (str): Nombre del alumno.
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.
    """
    media = calcular_media(nota1, nota2, nota3)
    estado = obtener_aprobado(media)
    calificacion = obtener_calificacion(media)

    # Se imprime la información del alumno de forma legible
    print(f"Alumno: {nombre_alumno}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Media: {media}")
    print(f"Resultado: {'Aprobado' if estado else 'Suspendido'}")
    print(f"Calificación: {calificacion}")
    print("----------------------")


def main():
    """
    Función principal que ejecuta ejemplos de informes de alumnos.
    """
    mostrar_informe_alumno("Ana García", 8, 7, 9)
    mostrar_informe_alumno("Luis Pérez", 4, 5, 3)
    mostrar_informe_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()