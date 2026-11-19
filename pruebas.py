from divisibilidad import es_par

# Pruebas para determinar si es par
def test_es_par_1():
    assert es_par(4) == True
    assert es_par(8) == True
    assert es_par(0) == True

def test_es_par_2():
    assert es_par(7) == False
    assert es_par(1) == False