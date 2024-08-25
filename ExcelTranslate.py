import pandas as pd
from googletrans import Translator

# Carregar o arquivo Excel
df = pd.read_excel('C:/Users/PICHAU/OneDrive/Área de Trabalho/ExcelTranslate/Arquivos/NGSL_1.2_with_English_definitions.xlsx', engine='openpyxl')

# Inicializar o tradutor
translator = Translator()

def traduzir_texto(texto, src='en', dest='pt'):
    if pd.isna(texto) or not texto.strip():
        return texto
    try:
        print(f'Tentando traduzir: {texto}')
        traduzido = translator.translate(texto, src=src, dest=dest)
        print(f'Texto traduzido: {traduzido.text}')
        return traduzido.text
    except Exception as e:
        print(f'Erro ao traduzir o texto: {e}')
        return texto

# Traduzir os dados da coluna 'Definitons' e adicionar a nova coluna 'Definições'
df['Definições'] = df['Definitons'].apply(lambda x: traduzir_texto(x))

# Salvar o resultado em um novo arquivo Excel
df.to_excel('2_with_English_definitions.xlsx', index=False)
