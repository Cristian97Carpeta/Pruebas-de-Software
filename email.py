import re

def validar_email(email):
    """
    Valida si un correo electrónico cumple con los requisitos especificados.

    Parámetros:
    email (str): El correo electrónico a validar.

    Retorna:
    bool: True si el correo es válido, False en caso contrario.
    """
    # patrón de expresión regular para validar el correo electrónico

    patron = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'

    # la función match de re para verificar si el email coincide con el patrón

    if re.match(patron, email):
        return True
    else:
        return False

# Función de prueba para validar la funcionalidad de validar_email

def test_validar_email():
    """
    Realiza pruebas unitarias para la función validar_email.
    """
    assert validar_email("juan.perez@empresa.com") == True, "Error: Esperaba True para 'juan.perez@empresa.com'"
    assert validar_email("maria@dominio") == False, "Error: Esperaba False para 'maria@dominio'"
    assert validar_email("pedro#2024@mail.org") == False, "Error: Esperaba False para 'pedro#2024@mail.org'"

test_validar_email()
print("Todas las pruebas pasaron exitosamente.")
