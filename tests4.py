from app4 import encontrar_maior

def test_numero_maior_esta_certo():
    numeros = [1,2,3,4,5,6,12]
    resultado_esperado = 12

    resultado = encontrar_maior(numeros)

    assert resultado==resultado_esperado

def test_numero_maior_esta_errado():
    numeros = [1,2,3,4,5,6,12]
    resultado_esperado = 5

    resultado = encontrar_maior(numeros)

    assert resultado!=resultado_esperado