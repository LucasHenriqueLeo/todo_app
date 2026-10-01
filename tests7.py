import pytest
from app7 import validar_idade

def test_se_idade_esta_valido():
    idade = 13
    resultadoesperado = True

    resultado = validar_idade(idade)

    assert resultado == resultadoesperado

def test_se_idade_esta_invalido():
    with pytest.raises(ValueError, match="A idade não pode ser negativa."):
    idade = -13
    resultadoesperado = False

    resultado = validar_idade(idade)

    assert resultado == resultadoesperado
