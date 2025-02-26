import re

def validar_telefono(numero):
    patron = r'^\+\d{2}-\d{3}-\d{3}-\d{4}$'
    return bool(re.match(patron, numero))

# Pruebas con assert
def test_validar_telefono():
    assert validar_telefono("+12-345-678-9012") == True  
    assert validar_telefono("12-345-678-9012") == False  
    assert validar_telefono("+123-456-789-0123") == False  
    assert validar_telefono("+12-3456-789-012") == False 


test_validar_telefono()
print("Pruebas satisfactoriamente aprobadas")