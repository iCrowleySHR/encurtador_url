<div align="center">

# Encurtador_URL
### FastAPI + SQLite + POO (Arquitetura em Camadas)

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

</div>

---

## 📘 Sobre o Projeto

O **URL Shortener API** é uma aplicação desenvolvida com **FastAPI** que permite encurtar URLs, redirecionar acessos e consultar estatísticas de uso.  
O projeto foi estruturado com **Programação Orientada a Objetos (POO)** e **arquitetura em camadas**, garantindo um código limpo, modular e fácil de manter.

---

## Tecnologias Utilizadas

- **FastAPI** — Framework backend moderno e performático  
- **SQLite** — Banco de dados leve e embutido  
- **SQLAlchemy** — ORM para mapeamento das entidades  
- **Pydantic** — Validação e tipagem dos dados  
- **Uvicorn** — Servidor ASGI rápido  
- **Docker** — Containerização e fácil deploy  

---

## Estrutura do Projeto

```bash
url_shortener/
│
├── app/
│   ├── core/              # Configurações centrais (banco, etc)
│   ├── models/            # Modelos ORM (SQLAlchemy)
│   ├── schemas/           # Schemas Pydantic (entrada e saída)
│   ├── repositories/      # Comunicação com o banco de dados
│   ├── services/          # Regras de negócio e lógica principal
│   ├── controllers/       # Rotas e integração com FastAPI
│   └── main.py            # Ponto de entrada da aplicação
│
├── requirements.txt
└── Dockerfile
```

---

## Como Executar Localmente

```bash
# 1️ Clonar o repositório
git clone https://github.com/icrowleyshr/encurtador_url.git
cd encurtador_url

# 2️ Instalar dependências
pip install -r requirements.txt

# 3️ Rodar o servidor
uvicorn app.main:app --reload
```

A aplicação estará disponível em:  
**http://127.0.0.1:8000**

---

## Endpoints Principais

### Criar URL Encurtada
**POST** `/urls/`

```json
{
  "url": "https://google.com"
}
```

<img width="1118" height="343" alt="image" src="https://github.com/user-attachments/assets/d6932bdc-bb9f-4398-88da-c31baa117c0d" />

### Redirecionar
**GET** `/urls/{code}`

### Estatísticas
**GET** `/urls/stats/{code}`

---

## Arquitetura

O projeto segue o padrão de **camadas independentes**, cada uma com uma responsabilidade única:

- **Models** → Representam as entidades do banco de dados (SQLAlchemy)  
- **Schemas** → Validação e tipagem dos dados (Pydantic)  
- **Repositories** → Manipulam o banco de dados  
- **Services** → Contêm as regras de negócio  
- **Controllers** → Definem as rotas e endpoints da API  
- **Core** → Configurações centrais (ex: banco, inicialização)

---

## Executar com Docker

```bash
# Build da imagem
docker build -t encurtador_url .

# Rodar o container
docker run -d -p 8000:8000 encurtador_url
```

---

## Licença

Este projeto está licenciado sob os termos da **MIT License** — sinta-se livre para usar e modificar.

---

<div align="center">
Feito com ❤️ em FastAPI e Python.
</div>
