def validar_email(email: str) -> bool:
 """Verifica se um endereço de e-mail é válido."""
 return "@" in email and "." in email