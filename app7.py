def validar_idade(idade: int) -> bool:
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")
    return True
