## 📌 Consulta de CEP com API ViaCEP

Este projeto foi desenvolvido em Python utilizando a biblioteca `CustomTkinter` para criar uma interface gráfica moderna e a API pública `ViaCEP` para realizar consultas de endereço através do CEP informado pelo usuário.

### 🚀 Como funciona

O usuário digita um CEP no campo de entrada da aplicação.
Após clicar no botão de consulta, o programa envia uma requisição para a API ViaCEP utilizando a biblioteca `requests`.

A API retorna os dados do endereço em formato JSON, contendo informações como:

* Logradouro
* Bairro
* Cidade
* Estado

Essas informações são exibidas diretamente na interface gráfica.

### 🌐 API utilizada

API pública: ViaCEP

Exemplo de requisição:

```python
url = f'http://viacep.com.br/ws/{cep}/json/'
```

### 🛠️ Tecnologias utilizadas

* Python
* CustomTkinter
* Requests
* API ViaCEP

## 🖼️ Interface do Programa

A aplicação possui uma interface gráfica simples e moderna desenvolvida com `CustomTkinter`, proporcionando uma melhor experiência visual para o usuário.

## 🖼️ Interface do Programa

A aplicação possui uma interface gráfica simples e moderna desenvolvida com `CustomTkinter`.

A tela contém:

* Campo para digitação do CEP
* Botão de consulta

<br>

<img width="597" height="478" alt="image" src="https://github.com/user-attachments/assets/ffa36a86-b7e3-425b-9617-21b3c008d59f" />

<br><br>

As imagens abaixo mostram o funcionamento da aplicação com o resultado exibido na interface:

<br>

<img width="602" height="479" alt="image" src="https://github.com/user-attachments/assets/04ecb805-44e9-4d8d-bb49-8ad797db1c3e" />




### 📚 Objetivo do projeto

O objetivo deste projeto foi praticar:

* Consumo de APIs
* Requisições HTTP
* Manipulação de JSON
* Interface gráfica com Python
* Tratamento básico de erros
