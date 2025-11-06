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
## Manifests

Você pode encontrar os Manifests da aplicação aqui:

<a href="https://github.com/iCrowleySHR/manifests-encurtador-url/"> https://github.com/iCrowleySHR/manifests-encurtador-url/ </a>

---

## Sobre o Projeto

O **Encurtador_URL** é uma aplicação desenvolvida com **FastAPI** que permite encurtar URLs, redirecionar acessos e consultar estatísticas de uso.  
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
##  Secrets

Antes, para o **Workflow** funcionar corretamente, você deve configurar as **secrets** no repositório, conforme mostrado nas imagens.

Essas *secrets* são variáveis de ambiente protegidas que o GitHub Actions utiliza para autenticar e executar as etapas do pipeline com segurança (por exemplo: deploy, acesso à API, banco de dados, etc.).

###  Como configurar
1. Acesse o repositório no GitHub.  
2. Vá em **Settings → Secrets and variables → Actions**.  
3. Clique em **New repository secret**.  
4. Adicione as *secrets* listadas abaixo (nomes e valores conforme sua configuração local ou conforme mostrado nas imagens).

<img width="1219" height="817" alt="image" src="https://github.com/user-attachments/assets/69c86503-4b0e-4347-945e-c6bde2a47e56" />

### Docker Hub e GitHub Token

Para que o workflow consiga autenticar e realizar o deploy corretamente, você precisa gerar e configurar dois tipos de tokens:  
um no **Docker Hub** e outro no **GitHub**.

---

#### Gerar Token no Docker Hub

1. Acesse: [https://hub.docker.com/settings/security](https://hub.docker.com/settings/security)
2. Vá até **Access Tokens**.
3. Clique em **New Access Token**.
4. Dê um nome (ex: `github-actions`) e defina o nível de permissão como **Read & Write**.
5. Clique em **Create**.
6. Copie o token gerado e salve-o temporariamente — ele **só aparecerá uma vez**.
7. No seu repositório no GitHub, adicione:
   - `DOCKER_USERNAME` → seu nome de usuário no Docker Hub  
   - `DOCKER_PASSWORD` → o token gerado no Docker Hub

<img width="1899" height="788" alt="image" src="https://github.com/user-attachments/assets/03941e6e-b076-4a46-8b62-593ffb117943" />


---

#### Gerar Token Pessoal no GitHub

1. Acesse: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Clique em **Generate new token → Fine-grained token** (ou **Classic token** se preferir).
3. Dê um nome (ex: `deploy-token`) e defina uma validade (ou deixe sem expiração).
4. Em **Repository access**, escolha:
   - **Only select repositories**, e selecione o repositório onde o deploy será feito.
5. Em **Permissions**, marque:
   - **Contents → Read and write**
   - **Actions → Read and write**
   - **Metadata → Read-only**
6. Clique em **Generate token**.
7. Copie o token e adicione no repositório como:
   - `PERSONAL_TOKEN` → o token pessoal do GitHub.

<img width="1885" height="893" alt="image" src="https://github.com/user-attachments/assets/c42c06c5-68ff-415f-9b6c-2608281520ff" />

---

#### Exemplo final de configuração no GitHub Secrets

| Nome da Secret      | Valor / Origem                            |
|---------------------|--------------------------------------------|
| `DOCKER_USERNAME`   | Seu usuário do Docker Hub                  |
| `DOCKER_PASSWORD`   | Token gerado em https://hub.docker.com     |
| `PERSONAL_TOKEN`    | Token gerado em https://github.com/settings/tokens |
| `DEPLOY_REPO`       | Repositório de destino do deploy (ex: `icrowleyshr/manifest_encurtador_url`) |

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
encurtador_url/
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

### Resultado Esperado

Após configurar corretamente as **secrets** e gerar os tokens do **Docker Hub** e **GitHub**, o seu **workflow** deve executar com sucesso.

O resultado esperado é:

- O GitHub Actions irá **buildar a imagem Docker**.  
- Em seguida, fará o **push automático** da imagem para o seu repositório no **Docker Hub**.  
- Você poderá visualizar a imagem publicada diretamente na sua conta do Docker Hub.

---

#### Em resumo:
✅ Workflow executando sem erros  
✅ Imagem gerada e enviada ao Docker Hub  
✅ Deploy automatizado funcionando corretamente  

---

#### Exemplo de resultado

O GitHub Actions mostrará algo como:

<img width="1899" height="876" alt="image" src="https://github.com/user-attachments/assets/1900f66d-b2ee-4757-8474-2193212bc166" />

E no Docker Hub, você verá a imagem publicada com sucesso:

<img width="1890" height="706" alt="image" src="https://github.com/user-attachments/assets/c73ec888-cdbf-42de-a29a-3d06f0ca757d" />

---

## Licença

Este projeto está licenciado sob os termos da **MIT License** — sinta-se livre para usar e modificar.

---

<div align="center">
Feito com ❤️ em FastAPI e Python.
</div>
