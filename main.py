import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# CONFIGURAÇÃO DE CAMINHOS (DINÂMICOS)
# ==========================================
# Obtém a pasta onde o script está guardado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define as pastas de entrada e saída relativas ao script
PASTA_ORIGEM = os.path.join(BASE_DIR, "fotos_originais")
PASTA_DESTINO = os.path.join(BASE_DIR, "fotos_finalizadas")
CAMINHO_TABELA = os.path.join(BASE_DIR, "base_dados_vencedores.xlsx")

# Garantir que as pastas existem
os.makedirs(PASTA_DESTINO, exist_ok=True)
os.makedirs(PASTA_ORIGEM, exist_ok=True)

def processar_branding_fotos():
    # ==========================================
    # LEITURA DA TABELA
    # ==========================================
    if not os.path.exists(CAMINHO_TABELA):
        print(f"[ERRO] Ficheiro Excel não encontrado: {CAMINHO_TABELA}")
        return

    df = pd.read_excel(CAMINHO_TABELA)

    # Nomes das colunas conforme a estrutura do projeto
    coluna_ficheiro = 'Nome_Do_Ficheiro'  
    coluna_autor = 'Autor'  

    # Mapeamento de ID da foto para o nome do Autor
    dados_fotos = {}
    for _, linha in df.iterrows():
        id_foto = str(linha[coluna_ficheiro]).strip().split('.')[0]
        autor = str(linha[coluna_autor]).strip()
        dados_fotos[id_foto] = autor

    # ==========================================
    # PROCESSAMENTO DAS IMAGENS
    # ==========================================
    ALTURA_BARRA = 100  # Altura da barra preta em píxeis
    
    print("A iniciar o processamento das fotos...\n")
    
    arquivos = [f for f in os.listdir(PASTA_ORIGEM) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    
    if not arquivos:
        print(f"Aviso: Nenhuma imagem encontrada na pasta: {PASTA_ORIGEM}")
        return

    for ficheiro in arquivos:
        # Extrai o identificador do nome do ficheiro (ex: "288")
        nome_puro = os.path.splitext(ficheiro)[0]
        
        # Procura o autor correspondente
        if nome_puro in dados_fotos:
            texto_assinatura = dados_fotos[nome_puro].upper()
        else:
            texto_assinatura = nome_puro.upper()
            print(f"Aviso: O código '{nome_puro}' não consta no Excel. A usar o nome do ficheiro.")

        # Abrir a imagem original
        img_path = os.path.join(PASTA_ORIGEM, ficheiro)
        with Image.open(img_path) as img:
            largura, altura = img.size
            
            # Criar nova tela adicionando espaço para a barra inferior
            nova_img = Image.new("RGB", (largura, altura + ALTURA_BARRA), "black")
            nova_img.paste(img, (0, 0))
            
            # Configuração do texto
            draw = ImageDraw.Draw(nova_img)
            tamanho_fonte = int(ALTURA_BARRA * 0.6) # Ajustado para margem de segurança
            
            try:
                # Tenta carregar uma fonte do sistema, caso contrário usa a padrão
                font = ImageFont.truetype("arial.ttf", tamanho_fonte)
            except IOError:
                font = ImageFont.load_default()

            # Posição: Centro da largura e centro da barra preta
            pos_x = largura / 2
            pos_y = altura + (ALTURA_BARRA / 2)
            
            # Renderizar assinatura
            draw.text((pos_x, pos_y), texto_assinatura, fill="white", font=font, anchor="mm")
            
            # Guardar resultado final
            caminho_salvar = os.path.join(PASTA_DESTINO, ficheiro)
            nova_img.save(caminho_salvar, quality=95)
            print(f"Sucesso: {ficheiro} assinado para {texto_assinatura}")

if __name__ == "__main__":
    processar_branding_fotos()
    print("\n--- Processo concluído! Verifica a pasta 'fotos_finalizadas' ---")
