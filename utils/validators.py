import re

def validar_email(email: str) -> bool:
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_senha(senha: str) -> bool:
    return len(senha) >= 8

def campos_preenchidos(email: str, senha: str) -> bool:
    return email.strip() != "" and senha.strip() != ""