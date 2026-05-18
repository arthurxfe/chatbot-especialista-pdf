# chatbot-especialista-pdf
Chatbot inteligente com IA capaz de responder perguntas com base em documentos PDF.

Este projeto implementa um chatbot inteligente capaz de responder perguntas com base no conteúdo de arquivos PDF.

O sistema utiliza LLMs para interpretar documentos e responder perguntas usando grounding, evitando respostas inventadas.

para executar vc precisa criar uma chave no groq API
---

## Tecnologias Utilizadas

- Python
- LangChain
- Groq API
- PyPDF2
- Prompt Engineering

---

## Arquitetura da Solução

Fluxo do sistema:

Usuário → Upload do PDF → Extração de Texto → Construção do Contexto → Modelo de IA → Resposta

---

## Como instalar no computador

### 1. Clone o projeto

git clone URL_DO_SEU_REPOSITORIO

### 2. Entre na pasta

cd chatbot-pdf-ia

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Configure a API

Crie um arquivo .env:

GROQ_API_KEY=sua-chave

### 5. Execute

python app.py

---

## Executar no Google Colab

Instale:

!pip install langchain-core langchain-groq PyPDF2 python-dotenv

Depois faça upload do arquivo app.py e execute normalmente.

---
## Desafios Superados

- Extração de texto de PDFs
- Controle de hallucinations
- Integração com LLMs
- Tratamento de erros

## Autor

Arthur Ribeiro Ferreira
