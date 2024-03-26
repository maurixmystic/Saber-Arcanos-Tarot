def tarot_arcana(day_of_birth):
    # Verificar si el día de nacimiento está entre 23 y 31
    if 23 <= day_of_birth <= 31:
        # Sumar los dígitos del día de nacimiento
        sum_of_digits = sum(int(digit) for digit in str(day_of_birth))
        # Determinar el arcano del tarot
        arcana = sum_of_digits % 22  # Hay 22 arcanos mayores
    else:
        # Si el día de nacimiento es menor que 23, corresponde directamente al arcano del tarot
        arcana = day_of_birth % 22

    # Diccionario de arcanos mayores y sus significados
    arcana_meanings = {
        1: "El Mago",
        2: "La Sacerdotisa",
        3: "La Emperatriz",
        4: "El Emperador",
        5: "El Hierofante",
        6: "Los Enamorados",
        7: "El Carro",
        8: "La Justicia",
        9: "El Ermitaño",
        10: "La Rueda de la Fortuna",
        11: "La Fuerza",
        12: "El Colgado",
        13: "La Muerte",
        14: "La Templanza",
        15: "El Diablo",
        16: "La Torre",
        17: "La Estrella",
        18: "La Luna",
        19: "El Sol",
        20: "El Juicio",
        21: "El Mundo",
        0: "El Loco"  # El arcano 0 es El Loco
    }

    # Devolver el significado del arcano del tarot
    return arcana_meanings.get(arcana, "Arcano desconocido")

# Solicitar al usuario que ingrese su día de nacimiento
try:
    day_of_birth = int(input("Por favor, ingresa tu día de nacimiento (1 a 31): "))
    if 1 <= day_of_birth <= 31:
        arcana_name = tarot_arcana(day_of_birth)
        print(f"El arcano mayor del tarot para alguien nacido el día {day_of_birth} es {arcana_name}.")
    else:
        print("El día ingresado no es válido. Por favor, ingresa un número entre 1 y 31.")
except ValueError:
    print("Por favor, ingresa un número válido.")