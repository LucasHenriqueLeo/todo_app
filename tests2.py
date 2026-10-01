from app2 import somar
from app2 import subtrair

def test_soma_deve_retornar_valor_esperado():
    a = 2
    b = 2
    resultado_esperado = 4

    resultado = somar(a, b)

    assert resultado==resultado_esperado

def test_soma_deve_retornar_valor_inesperado():
    a = 2
    b = 2
    resultado_esperado = 2 

    resultado = somar(a, b)

    assert resultado!=resultado_esperado

def test_subtracao_deve_retornar_valor_esperado():
    a = 4
    b = 2
    resultado_esperado = 2

    resultado = subtrair(a, b)

    assert resultado_esperado==resultado

def test_subtracao_deve_retornar_valor_inesperado():
    a = 2
    b = 2
    resultado_esperado = 1

    resultado = subtrair(a, b)

    assert resultado!=resultado_esperado