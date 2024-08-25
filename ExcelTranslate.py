import pandas as pd
from googletrans import Translator

# Carregar o arquivo Excel
# Se o arquivo usado estiver na pasta principal do projeto, só é necessário usar o nome do arquivo com a extenção
# Caso não esteja na pasta principal, utilize o caminho completo para o arquivo.
df = pd.read_excel('LOCAL_DO_ARQUIVO.xlsx', engine='openpyxl')

# Inicializar o tradutor
translator = Translator()

#Em 'src' você poderá escolher a linguagem que está o texto e em 'dest' você escolherá a linguaguem final
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
df.to_excel('NOME_DO_ARQUIVO_FINAL.xlsx', index=False)
