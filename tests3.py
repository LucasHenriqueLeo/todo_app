from app3 import eh_par

def test_numero_deve_retornar_par():
    numero = 2
    resultado_esperado = True

    resultado = eh_par(numero)

    assert resultado==resultado_esperado

def test_numero_deve_retornar_impar():
    numero = 3
    resultado_esperado = False

    resultado = eh_par(numero)

    assert resultado==resultado_esperado