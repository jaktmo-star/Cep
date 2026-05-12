import customtkinter as ctk
import requests

# Configurações visuais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Função consultar CEP
def consultar_cep():
    cep = entrada_cep.get().strip()

    url = f'http://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)
    dados = resposta.json()

    try:
        texto = (
            f"Logradouro: {dados['logradouro']}\n"
            f"Bairro: {dados['bairro']}\n"
            f"Cidade: {dados['localidade']}\n"
            f"Estado: {dados['uf']}"
        )

        resultado.configure(text=texto)

    except:
        resultado.configure(text="CEP não encontrado!")
        
       
# Criação da janela
janela = ctk.CTk()
janela.geometry("600x400")
janela.title("Consulta de CEP")

# Ícone da janela
# janela.iconbitmap('cep.ico')

# Título
titulo = ctk.CTkLabel(
    janela,
    text="Consulta de CEP",
    font=("Arial", 24)
)
titulo.pack(pady=20)

# Campo CEP
entrada_cep = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o CEP",
    width=300
)
entrada_cep.pack(pady=20)

# Botão consultar
botao = ctk.CTkButton(
    janela,
    text="Consultar",
    command=consultar_cep
)
botao.pack(pady=20)

# Resultado
resultado = ctk.CTkLabel(
    janela,
    text="",
    justify="left",
    font=("Arial", 16)
)
resultado.pack(pady=20)

# Loop da janela
janela.mainloop()