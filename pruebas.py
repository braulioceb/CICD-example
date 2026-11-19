from divisibilidad import es_impar

# Pruebas para determinar si es par
def test_es_impar_1():
    assert es_impar(4) == False
    assert es_impar(8) == False
    assert es_impar(0) == False
    

def test_es_impar_2():
    assert es_impar(7) == True
    assert es_impar(1) == True
    
# if __name__ == "__main__":
#     main()