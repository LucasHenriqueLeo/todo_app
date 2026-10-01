from app5 import eh_palindromo

def test_eh_palindromo_esta_certo():
    texto = "aba"
    resultado_esperado = True

    # Act
    resultado = eh_palindromo(texto)

    # Assert
    assert resultado == resultado_esperado

def test_eh_palindromo_esta_errado():
    texto = "tabua"
    resultado_esperado = False

    # Act
    resultado = eh_palindromo(texto)

    # Assert
    assert resultado == resultado_esperado

