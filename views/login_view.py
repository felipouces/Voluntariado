import tkinter as tk
from tkinter import messagebox
from services.auth_service import login

def iniciar_login_view():
    def fazer_login():
        email = email_entry.get()
        senha = senha_entry.get()
        sucesso, mensagem = login(email, senha)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", mensagem)

    janela = tk.Tk()
    janela.title("Tela de Login")
    janela.geometry("300x200")

    tk.Label(janela, text="Email:").pack(pady=5)
    email_entry = tk.Entry(janela, width=30)
    email_entry.pack()

    tk.Label(janela, text="Senha:").pack(pady=5)
    senha_entry = tk.Entry(janela, show="*", width=30)
    senha_entry.pack()

    logar_button = tk.Button(janela, text="Logar", command=fazer_login)
    logar_button.pack(pady=20)

    janela.mainloop()
