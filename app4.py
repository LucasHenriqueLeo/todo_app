def encontrar_maior(numeros: list) -> int:
    if not numeros:
        return None
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior
