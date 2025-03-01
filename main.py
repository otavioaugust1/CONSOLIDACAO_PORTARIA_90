from src.models.consolidacao import main as consolidacao
from src.models.relatorio import main as relatorio


def main():
    print('Executando consolidação de dados...')
    consolidacao()
    print('Executando geração de relatório...')
    relatorio()


if __name__ == '__main__':
    main()
