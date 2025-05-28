# Simulando banco de dados
USUARIOS_CADASTRADOS = {
    "usuario1@email.com": "senha123",
    "usuario2@email.com": "minhasenha"
}

def autenticar_usuario(email: str, senha: str) -> bool:
    return USUARIOS_CADASTRADOS.get(email) == senha