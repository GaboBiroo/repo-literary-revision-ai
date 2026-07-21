from docx import Document
import os

def verificar_capitulos(arquivo):
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo '{arquivo}' não encontrado.")
        return

    print(f"🔍 Auditando a estrutura de: {arquivo}\n")
    try:
        doc = Document(arquivo)
        contador = 0
        for p in doc.paragraphs:
            texto = p.text.strip()
            # Busca linhas que começam com "Capítulo" ou "Capitulo"
            if texto.lower().startswith("capítulo") or texto.lower().startswith("capitulo"):
                print(f"✅ Encontrado: {texto}")
                contador += 1
        
        print(f"\n📊 Total de capítulos mapeados: {contador}")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    verificar_capitulos("romance_revisado_final.docx")