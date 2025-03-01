# CONSOLIDACAO_PORTARIA_90

Este projeto é responsável por consolidar dados relacionados à **Portaria 90**, gerando relatórios e arquivos consolidados para auxiliar na gestão e análise das informações.

## Sobre a Portaria 90

A **Portaria GM/MS nº 90, de 6 de fevereiro de 2023**, estabelece diretrizes e critérios para a organização e funcionamento das redes de atenção à saúde no âmbito do Sistema Único de Saúde (SUS). Ela define normas e procedimentos para a implementação de políticas públicas de saúde, com foco na melhoria da qualidade e eficiência dos serviços prestados.

Para mais detalhes, consulte o texto oficial da Portaria 90:
- [Portaria GM/MS nº 90, de 6 de fevereiro de 2023](https://bvs.saude.gov.br/bvs/saudelegis/gm/2023/prt0090_06_02_2023.html)

## Funcionalidades

- **Consolidação de Dados**: Junta várias planilhas ou bases de dados em um único arquivo.
- **Geração de Relatórios**: Gera relatórios com base nos dados consolidados.

## Como Usar
### Pré-requisitos

- Python 3 instalado.
- Instale as dependências:

```bash
  pip install -r requirements.txt
```

## Executando o Projeto
1. Clone o repositório:

```bash
git clone https://github.com/otavioaugust1/CONSOLIDACAO_PORTARIA_90.git
cd CONSOLIDACAO_PORTARIA_90
```
2. Coloque os arquivos brutos na pasta data/raw.
3. Execute o projeto:

``` bash
python main.py
```
## Estrutura do Projeto
```
consolidacao_portaria_90/
├── docs/                     # Documentação do projeto
├── src/                      # Código-fonte
│   ├── controller/           # Lógica de controle
│   ├── models/               # Lógica de banco de dados
│   ├── views/                # Interface gráfica
│   ├── utils/                # Utilitários
│   └── app/                  # Configuração da aplicação
├── data/                     # Dados brutos e tratados
│   ├── raw/                  # Dados brutos baixados ou recebidos
│   ├── processed/            # Dados tratados
│   └── results/              # Resultados da consolidação
├── tests/                    # Testes
├── README.md                 # Documentação principal
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos ignorados pelo Git
└── main.py                   # Ponto de entrada do projeto
```

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Abra uma issue ou envie um pull request!

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

