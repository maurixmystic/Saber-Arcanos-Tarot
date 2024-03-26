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

    # Devolver el arcano del tarot
    return arcana

# Ejemplo de uso:
day_of_birth = 1  # Reemplazar con el día real de nacimiento
arcana = tarot_arcana(day_of_birth)
print(f"El arcano mayor del tarot para alguien nacido el día {day_of_birth} es el número {arcana}.")