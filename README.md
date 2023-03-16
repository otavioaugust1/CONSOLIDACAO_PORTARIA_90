# 🛠️ Bot consolidador de planilhas de cirurgias eletivas

![Badge em Desenvolvimento](https://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge)

![GitHub Org's stars](https://img.shields.io/github/stars/camilafernanda?style=social)

O objetivo deste bot é consolidar as planilhas de cirurgias eletivas enviadas de acordo com a Portaria 90, verificando se os dados estão em conformidade com as exigências da portaria.

## Funcionalidades

* Leitura das planilhas da pasta especificada
* Consolidação dos dados em um único DataFrame
* Verificação da conformidade dos dados com a Portaria 90
* Renomeação e exclusão de colunas e linhas desnecessárias

## Requisitos

Para utilizar o bot, é necessário ter os seguintes requisitos instalados:
* Python 3.x
* Bibliotecas pandas, time, os, locale e xlsxwriter

## Como utilizar

Para utilizar o bot, siga as instruções abaixo:
1. Faça o download ou clone este repositório
2. Abra o terminal e navegue até a pasta do repositório
3. Realize o download dos planos no SAIPS (arquivo. xlsx)
4. Renomeie as planilhas com o nome das UF (ex. BAHIA, SÃO PAULO, entre outros)
5. Insira as planilhas na pasta "BASE"
6. Execute o script utilizando o comando python "consolidar.ipynb" 
7. Aguarde o término da execução do script
8. A base consolidada com todas as planilhas (.xlsx) estará na pasta "PLANILHA"

# Resultado

Ao final da execução do script, serão gerados 4 arquivos:
* 1 arquivo '.xlsx' com o nome "BASE_G" com 3 abas
* 1 arquivo '.csv' com as informações da primeira aba 
* 1 arquivo '.csv' com as informações da segunda aba 
* 1 arquivo '.csv' com as informações da terceira aba 

## Observações
* Certifique-se de que todas as planilhas estejam no formato ".xlsx"
* Certifique-se de que as planilhas estejam na pasta especificada
* Este bot foi desenvolvido em Jupyter Notebook, mas pode ser executado em qualquer ambiente Python 3.x
* Este projeto está sob a licença MIT License.

 
