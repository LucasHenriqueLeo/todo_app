from app1 import validar_email


def test_validar_email_deve_retornar_valido():
    # Arrange / SetUp
    email = 'lucashenriqueleonardodejesus@gmail.com'
    resultado_esperado = True

    # Act
    resultado = validar_email(email)

    # Assert
    assert resultado == resultado_esperado

def test_validar_email_deve_retornar_invalido():
    # Arrange / SetUp
    email = 'lucashenriqueleonardogmailcom'
    resultado_esperado = False

    # Act
    resultado = validar_email(email)

    # Assert
    assert resultado == resultado_esperado