from app6 import celsius_para_fahrenheit

def test_conversao_esta_correta():
    tempcelsius = 10
    resultado_esperado = 50

    # Act
    resultado = celsius_para_fahrenheit(tempcelsius)

    # Assert
    assert resultado == resultado_esperado

def test_conversao_esta_incorreta():
    tempcelsius = 12
    resultado_esperado = 0

    # Act
    resultado = celsius_para_fahrenheit(tempcelsius)

    # Assert
    assert resultado != resultado_esperado