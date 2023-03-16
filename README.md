# 🛠️ Bot consolidador de planilhas de cirurgias eletivas

![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge)

![GitHub Org's stars](https://img.shields.io/github/stars/camilafernanda?style=social)

Este bot tem como objetivo consolidar as planilhas enviadas de acordo com a Portaria 90. Ele é capaz de analisar os dados enviados e verificar se estão em conformidade com as exigências da portaria.

## Funcionalidades

* Leitura das planilhas da pasta especificada
* Consolidação dos dados em um único DataFrame
* Verificação da conformidade dos dados com a Portaria 90
* Renomeação e exclusão de colunas e linhas desnecessárias
* Exclusão de linhas sem valor na coluna "PROCEDIMENTO CIRÚRGICO"
* Exclusão de linhas com valor "TOTAL" na coluna "PROCEDIMENTO CIRÚRGICO"

## Requisitos
* Python 3.x
* Bibliotecas pandas, time, os e xlsxwriter

## Como utilizar
1. Faça o download ou clone este repositório
2. Abra o terminal e navegue até a pasta do repositório
3. Execute o script bot_consolidador_cirurgias_eletivas.py utilizando o comando python bot_consolidador_cirurgias_eletivas.py
4. Insira a pasta contendo as planilhas quando solicitado pelo script
5. Aguarde o término da execução do script

## Observações
* Certifique-se de que todas as planilhas estejam no formato .xlsx
* Certifique-se de que as planilhas estejam na pasta especificada
* Este bot foi desenvolvido em Jupyter Notebook, mas pode ser executado em qualquer ambiente Python 3.x
* Este projeto está sob a licença MIT License.

 
