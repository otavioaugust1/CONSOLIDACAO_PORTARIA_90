import os

import pandas as pd


def gerar_relatorio(df, pasta_results):
    # Gera um relatório com estatísticas e informações detalhadas
    relatorio = f"""
    ============ RELATÓRIO DE DADOS CONSOLIDADOS ============
    Total de Registros: {len(df)}
    Colunas Disponíveis: {', '.join(df.columns)}
    Estatísticas Descritivas:
    {df.describe().to_string()}
    """
    caminho_relatorio = os.path.join(pasta_results, 'relatorio.txt')
    with open(caminho_relatorio, 'w') as f:
        f.write(relatorio)


def main():
    pasta_processed = 'data/processed'
    pasta_results = 'data/results'

    caminho_dados = os.path.join(pasta_processed, 'dados_consolidados.csv')

    # Verifica se o arquivo consolidado existe
    if not os.path.exists(caminho_dados):
        print(
            '[ERRO] Arquivo consolidado não encontrado. Execute a consolidação primeiro.'
        )
        return

    try:
        df = pd.read_csv(caminho_dados, sep=';', encoding='latin-1')
        gerar_relatorio(df, pasta_results)
        print('[OK] Relatório gerado com sucesso.')
    except Exception as e:
        print(f'[ERRO] Falha ao gerar o relatório: {e}')


if __name__ == '__main__':
    main()
