# Informações

## Descrição

Este projeto fornece um **CLI (Interface de Linha de Comando) para gerenciar bancos e coleções MongoDB**, permitindo listar bancos, listar coleções e criar novas coleções.

O projeto utiliza:

* **Python**
* **PyMongo**
* **python-dotenv** para carregar a URL do MongoDB a partir de um arquivo `.env`.

## Como usar

### Passo 0 — Criar e ativar o ambiente virtual

No terminal execute:

```powershell
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### Passo 1 — Instalar dependências

Instale os pacotes necessários a partir do `requirements.txt`:

```powershell
pip install -r requirements.txt
```

### Passo 2 — Configurar o `.env`

Crie um arquivo chamado `.env` dentro da pasta do projeto (`Semana5`) e adicione a variável com a URL do seu MongoDB Atlas:

```env
URL="sua_string_de_conexao_mongodb"
```

> Substitua `"sua_string_de_conexao_mongodb"` pelo link real do seu MongoDB Atlas.

### Passo 3 — Rodar o CLI

No terminal, ainda dentro da pasta `Semana5`, execute o CLI:

```powershell
py main.py
```

## Funcionalidades do CLI

1. **Listar todos os bancos**
   Mostra todos os bancos disponíveis no cluster MongoDB.

2. **Listar coleções de um banco**
   Mostra todas as coleções dentro de um banco específico.

3. **Adicionar nova coleção**
   Permite criar uma nova coleção em um banco.

0. **Sair**
   Encerra o CLI.
