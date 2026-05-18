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

## Como Executar

### 1. Clone o projeto

```bash
git clone <seu-repositorio>
```

### 2. Instale dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a API

Crie um arquivo `.env`:

```env
GROQ_API_KEY=sua_chave
```

### 4. Execute

```bash
python src/chatbot.py
```

---

## Desafios Superados

- Extração de texto de PDFs
- Controle de hallucinations
- Integração com LLMs
- Tratamento de erros

---
##codigo do projeto
# ============================================================
# INSTALAÇÃO DAS BIBLIOTECAS (execute no Google Colab se necessário)
# ============================================================
!pip install langchain-core langchain-groq PyPDF2

# ============================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ============================================================
import os
from PyPDF2 import PdfReader
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# ============================================================
# CONFIGURAÇÃO DA API GROQ
# ============================================================
# IMPORTANTE: coloque sua chave da API abaixo
os.environ["GROQ_API_KEY"] = "  "

# ============================================================
# VERIFICAR SE ESTÁ NO GOOGLE COLAB E FAZER UPLOAD DO PDF
# ============================================================
print("Sistema: Verificando ambiente...")

try:
    from google.colab import files
    print("Sistema: Ambiente Google Colab detectado.")
    print("Sistema: Faça o upload do seu arquivo PDF.")

    uploaded = files.upload()

    # Pega o nome do arquivo enviado
    nome_arquivo = list(uploaded.keys())[0]

except:
    print("Sistema: Não está no Google Colab.")
    nome_arquivo = input("Digite o caminho do arquivo PDF: ")

# ============================================================
# LEITURA DO PDF
# ============================================================
print("Sistema: Lendo o arquivo PDF...")

try:
    leitor_pdf = PdfReader(nome_arquivo)
    contexto_pdf = ""

    # Percorre todas as páginas do PDF
    for pagina in leitor_pdf.pages:
        texto = pagina.extract_text()
        if texto:
            contexto_pdf += texto + "\n"

    # Verifica se o conteúdo foi extraído
    if contexto_pdf.strip() == "":
        print("Erro: Não foi possível extrair texto do PDF.")
    else:
        print("Sistema: PDF carregado com sucesso!")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho.")
    contexto_pdf = ""

# ============================================================
# CRIAÇÃO DO PROMPT (GROUNDING)
# ============================================================
prompt = ChatPromptTemplate.from_template("""
Você é um assistente que responde perguntas APENAS com base no texto abaixo.

REGRAS:
- Use somente as informações do contexto.
- NÃO use conhecimento externo.
- NÃO invente respostas.
- Se a resposta não estiver no texto, diga:
"Não encontrei essa informação no documento fornecido."

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
""")

# ============================================================
# CONFIGURAÇÃO DO MODELO
# ============================================================
print("Sistema: Carregando modelo de IA...")

modelo = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ============================================================
# INÍCIO DO CHAT
# ============================================================
print("\nSistema: Chat iniciado! Digite 'x' para sair.\n")

while True:
    pergunta = input("Você: ")

    # Condição de saída
    if pergunta.lower() == "x":
        print("\nSistema: Muito obrigado por usar a Minha_IA. Sessão encerrada.")
        break

    # Verifica se o contexto existe
    if contexto_pdf.strip() == "":
        print("Sistema: Não há conteúdo para responder.")
        continue

    try:
        # Monta a cadeia de execução
        cadeia = prompt | modelo

        # Gera resposta
        resposta = cadeia.invoke({
            "contexto": contexto_pdf,
            "pergunta": pergunta
        })

        # Exibe resposta
        print("IA:", resposta.content)

    except Exception as erro:
        print("Erro ao processar a pergunta:", erro)

## Autor

Arthur Ribeiro Ferreira
