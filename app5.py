def eh_palindromo(texto: str) -> bool:
 """Verifica se uma string é um palíndromo."""
 texto = texto.lower().replace(" ", "")
 return texto == texto[::-1]