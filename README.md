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

<div align="center">

# Encurtador_URL
### FastAPI + SQLite + POO (Arquitetura em Camadas)

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![CI/CD](https://img.shields.io/github/actions/workflow/status/icrowleyshr/encurtador_url/ci-cd.yml?label=CI%2FCD&logo=github)

</div>

---

## 📘 Sobre o Projeto

O **URL Shortener API** é uma aplicação desenvolvida com **FastAPI** que permite encurtar URLs, redirecionar acessos e consultar estatísticas de uso.  
O projeto foi estruturado com **Programação Orientada a Objetos (POO)** e **arquitetura em camadas**, garantindo um código limpo, modular e fácil de manter.

---

##  Integração Contínua (CI/CD)

O projeto conta com um pipeline automatizado utilizando **GitHub Actions**, responsável por:

- Fazer build da imagem Docker a cada push na branch `main`
- Fazer login no **Docker Hub** com credenciais seguras (armazenadas em `GitHub Secrets`)
- Enviar (push) a nova imagem para o Docker Hub
- Atualizar o arquivo `deployment.yaml` em outro repositório de deploy (via token pessoal)

### Arquivo do Workflow (`.github/workflows/ci-cd.yml`)

```yaml
name: CI/CD Encurtador URL

on:
  push:
    branches: ["main"]

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout código da aplicação
        uses: actions/checkout@v4

      - name: Login no Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build e Push da imagem Docker
        run: |
          IMAGE=${{ secrets.DOCKER_USERNAME }}/encurtador-url
          TAG=$(date +%s)
          docker build -t $IMAGE:$TAG .
          docker push $IMAGE:$TAG
          echo "IMAGE=$IMAGE:$TAG" >> $GITHUB_ENV

      - name: Checkout repositório de manifests
        uses: actions/checkout@v4
        with:
          repository: ${{ secrets.DEPLOY_REPO }}
          token: ${{ secrets.PERSONAL_TOKEN }}
          path: manifests

      - name: Atualizar imagem no deployment.yaml
        run: |
          cd manifests
          sed -i "s|image: .*|image: $IMAGE|" deployment.yaml
          git config --global user.email "actions@github.com"
          git config --global user.name "GitHub Actions"
          git add deployment.yaml
          git commit -m "Atualiza imagem para $IMAGE" || echo "Sem alterações"
          git push
```

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

![Vídeo-sem-título-‐-Feito-com-o-Clipchamp](https://github.com/user-attachments/assets/274a9fb7-ff9b-4739-afe9-4f0f9cc5da78)


### Estatísticas
**GET** `/urls/stats/{code}`

<img width="608" height="237" alt="image" src="https://github.com/user-attachments/assets/b0e7550f-2820-4673-a945-95e024c2a703" />


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
