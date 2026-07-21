from google import genai

API_KEY = "SUA_CHAVE_AQUI"

client = genai.Client(api_key=API_KEY)

print("🔍 Consultando a lista de modelos liberados para a sua conta...\n")
try:
    for model in client.models.list():
        if "gemini" in model.name.lower():
            print(f"✅ {model.name}")
except Exception as e:
    print(f"❌ Erro ao consultar: {e}")
