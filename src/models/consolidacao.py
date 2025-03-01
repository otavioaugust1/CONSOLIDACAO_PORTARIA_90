import os

import pandas as pd


def carregar_dados(pasta_raw):
    # Carrega os dados brutos da pasta raw
    arquivos = os.listdir(pasta_raw)
    dados = []
    for arquivo in arquivos:
        if arquivo.endswith('.xlsx') or arquivo.endswith('.csv'):
            caminho = os.path.join(pasta_raw, arquivo)
            if arquivo.endswith('.xlsx'):
                df = pd.read_excel(caminho)
            else:
                df = pd.read_csv(caminho, sep=';', encoding='latin-1')
            dados.append(df)
    return dados


def consolidar_dados(dados):
    # Consolida os dados em um único DataFrame
    df_consolidado = pd.concat(dados, ignore_index=True)
    return df_consolidado


def salvar_dados_consolidados(df, pasta_processed):
    # Salva os dados consolidados em um arquivo CSV
    caminho_saida = os.path.join(pasta_processed, 'dados_consolidados.csv')
    df.to_csv(caminho_saida, sep=';', encoding='latin-1', index=False)


def main():
    pasta_raw = 'data/raw'
    pasta_processed = 'data/processed'

    dados = carregar_dados(pasta_raw)
    df_consolidado = consolidar_dados(dados)
    salvar_dados_consolidados(df_consolidado, pasta_processed)


def main():
    pasta_raw = 'data/raw'
    pasta_processed = 'data/processed'

    try:
        dados = carregar_dados(pasta_raw)
        if dados:
            df_consolidado = consolidar_dados(dados)
            salvar_dados_consolidados(df_consolidado, pasta_processed)
            print('[OK] Consolidação concluída com sucesso.')
        else:
            print('[ERRO] Nenhum dado foi carregado para consolidação.')
    except Exception as e:
        print(f'[ERRO] Falha durante a consolidação: {e}')


if __name__ == '__main__':
    main()
