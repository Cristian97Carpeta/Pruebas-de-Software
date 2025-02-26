def calcular_puntuacion(puntos, bonus):
    """
    Calcula la puntuación basada en los puntos y el estado del bonus.

    Parámetros:
    puntos (int): La cantidad de puntos obtenidos.
    bonus (bool): Indica si el bonus está activo o no.

    Retorna:
    str: La calificación correspondiente ("Oro", "Plata" o "Bronce").
    """

    if puntos >= 100 and bonus:
        return "Oro"

    elif puntos >= 50 and puntos < 100:
        return "Plata"

    else:
        return "Bronce"

def test_calcular_puntuacion():
    """
    Realiza pruebas para la función calcular_puntuacion.
    """
    assert calcular_puntuacion(100, True) == "Oro", "Error: Esperaba 'Oro' para (100, True)"
    assert calcular_puntuacion(100, False) == "Bronce", "Error: Esperaba 'Bronce' para (100, False)"
    assert calcular_puntuacion(50, True) == "Plata", "Error: Esperaba 'Plata' para (50, True)"
    assert calcular_puntuacion(49, False) == "Bronce", "Error: Esperaba 'Bronce' para (49, False)"


test_calcular_puntuacion()
print("TODAS LAS PRUEBAS HAN SIDO COMPROBADAS SATISFACTORIAMENTE")
