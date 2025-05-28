from repository.usuario_repo import autenticar_usuario
from utils.validators import validar_email, validar_senha, campos_preenchidos

def login(email: str, senha: str):
    if not campos_preenchidos(email, senha):
        return False, "Preencha todos os campos."

    if not validar_email(email):
        return False, "Formato de email inválido."

    if not validar_senha(senha):
        return False, "A senha deve ter pelo menos 8 caracteres."

    if autenticar_usuario(email, senha):
        return True, "Login realizado com sucesso."
    
    return False, "Usuário ou senha inválidos."
