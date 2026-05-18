import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# ============================================
# CARREGAR VARIÁVEIS DE AMBIENTE
# ============================================
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("Erro: API não encontrada.")
    exit()

# ============================================
# DETECTAR COLAB OU COMPUTADOR
# ============================================
print("Sistema iniciado...")

try:
    from google.colab import files

    print("Google Colab detectado.")
    uploaded = files.upload()
    nome_arquivo = list(uploaded.keys())[0]

except:
    print("Modo computador.")
    nome_arquivo = input("Digite o caminho do PDF: ")

# ============================================
# LER PDF
# ============================================
contexto_pdf = ""

try:
    leitor_pdf = PdfReader(nome_arquivo)

    for pagina in leitor_pdf.pages:
        texto = pagina.extract_text()

        if texto:
            contexto_pdf += texto + "\n"

except:
    print("Erro ao ler PDF.")
    exit()

# ============================================
# PROMPT
# ============================================
prompt = ChatPromptTemplate.from_template("""
Você responde usando SOMENTE o contexto abaixo.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

Se não encontrar a resposta, diga:
"Não encontrei essa informação no documento."
""")

# ============================================
# MODELO
# ============================================
modelo = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# ============================================
# CHAT
# ============================================
print("\nChat iniciado. Digite x para sair.\n")

while True:

    pergunta = input("Você: ")

    if pergunta.lower() == "x":
        print("Sessão encerrada.")
        break

    cadeia = prompt | modelo

    resposta = cadeia.invoke({
        "contexto": contexto_pdf,
        "pergunta": pergunta
    })

    print("IA:", resposta.content)
