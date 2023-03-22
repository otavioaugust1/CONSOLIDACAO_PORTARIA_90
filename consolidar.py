# Bot consolidador de planilhas de cirurgias eletivas
## Autor: Otávio Augusto dos Santos
## Data: 2023-03-17

## Versão: 1.0
## Descrição: Consolida dados de cirurgias eletivas (Planilhas) em um único arquivo
## Entrada: Dados do SAIPS (Planilhas)
## Saída: Dados consolidados (Planilhas)
## Observações:
## 1. O arquivo de entrada deve estar na pasta BASE 
## 2. O arquivo de saída será gerado no formato CSV e XLSX
## 3. O arquivo de saída será salvo na pasta de PLANILHA

# Importando bibliotecas
import pandas as pd # Manipulação de dados
import os # Manipulação de arquivos
import time # Controle de tempo
import xlsxwriter # Manipulação de planilhas
import locale # Manipulação de dados
import warnings # Manipulação de dados
warnings.filterwarnings("ignore") # Ignorar avisos
tempo_inicial = time.time() # Inicia o contador de tempo
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Configura o locale para pt_BR
pd.set_option('display.max_columns', None) # Configura o pandas para mostrar todas as colunas
pd.set_option('display.max_rows', None) # Configura o pandas para mostrar todas as linhas

# Criar pasta de saída e de log
pasta_saida = 'PLANILHA T' # Pasta de saída

try:
    os.makedirs(pasta_saida, exist_ok=True)
    print(f'[OK] Pasta {pasta_saida} criada com sucesso:=========> {time.time() - tempo_inicial:.2f} segundos')
except OSError as error:
    print(f'[ERRO] Falha ao criar pasta {pasta_saida} - {error}:====> {time.time() - tempo_inicial:.2f} segundos')

arquivo_log = open(f'{pasta_saida}/LOG.txt', 'w') # Arquivo de log

# Importação das planilhas
## ABA 1

pasta = 'BASE' # Pasta de entrada
arquivos = os.listdir(pasta) # Lista os arquivos da pasta de entrada
dfs_dict = {} # Dicionário para armazenar os dataframes
aba1 = 'Ident. Fila na UF' # Nome da aba1
for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith('.xlsx'):
        nome_arquivo = os.path.splitext(arquivo)[0]
        df_aba1 = pd.read_excel(caminho_arquivo, sheet_name=aba1, skiprows=1, header=0, dtype=str)
        df_aba1['UF'] = nome_arquivo
        dfs_dict[nome_arquivo] = df_aba1
df_planilha_aba1 = pd.concat(dfs_dict.values(), ignore_index=True) # Concatena os dataframes
print(f"[OK] Planilha {aba1} importada com sucesso:===========> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução

## ABA 1 - tratamento de dados
df_planilha_aba1.rename(columns={'PLANO ESTADUAL DE REDUÇÃO DE FILAS DE ESPERA EM CIRURGIAS ELETIVAS - FILA DE ESPERA':'CÓDIGO DO PROCEDIMENTO NO SIGTAP','Unnamed: 1':'PROCEDIMENTO CIRÚRGICO','Unnamed: 2':'QUANTIDADE DE SOLICITAÇÕES NA FILA ATÉ DIA 31/12/22', 'Unnamed: 3':'Redução do Tamanho da Fila (%)', 'Unnamed: 4':'Prazo para reduzir o % proposto (em meses)', 'Unnamed: 5':'Qtde de cirurgias a serem feitas no prazo pactuado', 'Unnamed: 6':'SQ (CODIGO Interno', 'UF':'UF'} , inplace=True) # Renomeia as colunas

df_planilha_aba1.drop([0,1], inplace=True) # Exclui as linhas 0 e 1
df_planilha_aba1.dropna(subset=['PROCEDIMENTO CIRÚRGICO'], inplace=True) # Exclui as linhas que não possuem valor na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba1.drop(df_planilha_aba1[df_planilha_aba1['PROCEDIMENTO CIRÚRGICO'] == 'TOTAL'].index, inplace=True) # Exclui as linhas que possuem valor 'TOTAL' na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba1.drop(df_planilha_aba1[df_planilha_aba1['PROCEDIMENTO CIRÚRGICO'] == 'PROCEDIMENTO CIRÚRGICO'].index, inplace=True) # Exclui as linhas que possuem valor 'TOTAL' na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba1['Qtde de cirurgias a serem feitas no prazo pactuado'].fillna(0, inplace=True)
df_planilha_aba1['Qtde de cirurgias a serem feitas no prazo pactuado'] = df_planilha_aba1['Qtde de cirurgias a serem feitas no prazo pactuado'].astype(int)# Converte a coluna 'Qtde de cirurgias a serem feitas no prazo pactuado' para inteiro
print(f"[OK] Planilha {aba1} tratada com sucesso:=============> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução


## ABA 2
pasta = 'BASE'  # Pasta de entrada
arquivos = os.listdir(pasta) # Lista os arquivos da pasta de entrada
dfs_dict = {} # Dicionário para armazenar os dataframes
aba2 = 'Ident. CNES e Proced.' # Nome da aba2
for arquivo in arquivos: 
    caminho_arquivo = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith('.xlsx'):
        nome_arquivo = os.path.splitext(arquivo)[0]
        df_aba2 = pd.read_excel(caminho_arquivo, sheet_name=aba2, skiprows=1, header=0, dtype=str)
        df_aba2['UF'] = nome_arquivo
        dfs_dict[nome_arquivo] = df_aba2
df_planilha_aba2 = pd.concat(dfs_dict.values(), ignore_index=True) # Concatena os dataframes
print(f"[OK] Planilha {aba2} importada com sucesso:===========> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução

## ABA 2 - tratamento de dados
df_planilha_aba2.rename(columns={'PLANO ESTADUAL DE REDUÇÃO DE FILAS DE ESPERA EM CIRURGIAS ELETIVAS - CNES':'CNES','Unnamed: 1':'ESTABELECIMENTO','Unnamed: 2':'CÓDIGO DO PROCEDIMENTO PRINCIPAL NO SIGTAP', 'Unnamed: 3':'PROCEDIMENTO CIRÚRGICO (PRINCIPAL)', 'Unnamed: 4':'COMPLEMENTO COM RECURSO FEDERAL DO PROCEDIMENTO PRINCIPAL (Percentual)', 'Unnamed: 5':'GESTÃO DO SERVIÇO', 'Unnamed: 6':'CODIGO DA NATUREZA JURÍDICA','Unnamed: 7':'NATUREZA JURÍDICA', 'Unnamed: 8':'POSSUI CONTRATO COM A SECRETARIA DE SAÚDE ?', 'Unnamed: 9':'Identificação do Nome do Estabelecimento que não apareceu nesta planilha (coluna B)','Unnamed: 10':'SQ (CODIGO Interno'}, inplace=True)  # Renomeia as colunas

df_planilha_aba2.drop([0,1], inplace=True) # Exclui as linhas 0 e 1
df_planilha_aba2.dropna(subset=['ESTABELECIMENTO'], inplace=True) # Exclui as linhas que não possuem valor na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba2.drop(df_planilha_aba2[df_planilha_aba2['ESTABELECIMENTO'] == 'ESTABELECIMENTO'].index, inplace=True) # Exclui as linhas que possuem valor 'TOTAL' na coluna 'PROCEDIMENTO CIRÚRGICO'
print(f"[OK] Planilha {aba2} tratada com sucesso:=============> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução


## ABA 3
pasta = 'BASE'  # Pasta de entrada
arquivos = os.listdir(pasta) # Lista os arquivos da pasta de entrada
dfs_dict = {} # Dicionário para armazenar os dataframes
aba3 = 'Ident. CNES e Proced.' # Nome da aba3
for arquivo in arquivos: 
    caminho_arquivo = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho_arquivo) and caminho_arquivo.endswith('.xlsx'):
        nome_arquivo = os.path.splitext(arquivo)[0]
        df_aba3 = pd.read_excel(caminho_arquivo, sheet_name=aba3, skiprows=1, header=0, dtype=str)
        df_aba3['UF'] = nome_arquivo
        dfs_dict[nome_arquivo] = df_aba3
df_planilha_aba3 = pd.concat(dfs_dict.values(), ignore_index=True) # Concatena os dataframes
print(f"[OK] Planilha {aba3} importada com sucesso:===========> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução

## ABA 3 - tratamento de dados
df_planilha_aba3.rename(columns={'Distribuição e Cronograma da Execução do Recurso Financeiro':'CODIGO GESTOR','Unnamed: 1':'Gestão do Recurso','Unnamed: 2':'DESCRIÇÃO DO GESTOR','Unnamed: 3':'VALOR','Unnamed: 4':'março','Unnamed: 5':'abril','Unnamed: 6':'maio','Unnamed: 7':'junho','Unnamed: 8':'julho','Unnamed: 9':'agosto','Unnamed: 10':'setembro','Unnamed: 11':'outubro','Unnamed: 12':'novembro','Unnamed: 13':'dezembro','Unnamed: 14':'% TOTAL','SQ (CODIGO Interno':'SQ (CODIGO Interno'}, inplace=True) # Renomeia as colunas

df_planilha_aba3.drop(df_planilha_aba3.index[0:6], inplace=True) # Remove as 5 primeiras linhas do arquivo
df_planilha_aba3.dropna(subset=['CODIGO GESTOR'], inplace=True) # Exclui as linhas que não possuem valor na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba3.drop(df_planilha_aba3[df_planilha_aba3['CODIGO GESTOR'] == 'CODIGO GESTOR'].index, inplace=True) # Exclui as linhas que possuem valor 'TOTAL' na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba3.dropna(subset=['% TOTAL'], inplace=True) # Exclui as linhas que não possuem valor na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba3.dropna(subset=['DESCRIÇÃO DO GESTOR'], inplace=True) # Exclui as linhas que não possuem valor na coluna 'PROCEDIMENTO CIRÚRGICO'
df_planilha_aba3['VALOR'] = df_planilha_aba3['VALOR'].map(lambda x: locale.currency(float(x), grouping=True)) # Formata a coluna 'VALOR' para moeda

cols = ["março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", "% TOTAL"] # Define as colunas que serão formatadas
df_planilha_aba3[cols] = df_planilha_aba3[cols].fillna(0).astype(float) # Converte os valores para float
df_planilha_aba3[cols] = df_planilha_aba3[cols].applymap(lambda x: '{:.0%}'.format(float(x))) # Formata as colunas para porcentagem
print(f"[OK] Planilha {aba3} tratada com sucesso:=============> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução

## Salva o arquivo
## EXCEL

writer = pd.ExcelWriter(f'{pasta_saida}/BASE_G.xlsx', engine='xlsxwriter') # Cria um arquivo excel
df_planilha_aba1.to_excel(writer, sheet_name='Ident. Fila na UF', index=False)
df_planilha_aba2.to_excel(writer, sheet_name='Ident. CNES e Proced.', index=False)
df_planilha_aba3.to_excel(writer, sheet_name='Execução', index=False)
writer.save()
print(f"[OK] Arquivo {pasta_saida}/BASE_G.xlsx salvo com sucesso:===> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução

## CSV
df_planilha_aba1.to_csv('PLANILHA/BASE_G_1.csv', sep=';', encoding='latin-1', index=False) # Cria um arquivo csv
df_planilha_aba2.to_csv('PLANILHA/BASE_G_2.csv', sep=';', encoding='latin-1', index=False) # Cria um arquivo csv
df_planilha_aba3.to_csv('PLANILHA/BASE_G_3.csv', sep=';', encoding='latin-1', index=False) # Cria um arquivo csv
print(f"[OK] Arquivos {pasta_saida}/BASE_G_1.csv, {pasta_saida}/BASE_G_2.csv e {pasta_saida}/BASE_G_3.csv salvos com sucesso:===> {time.time() - tempo_inicial:.2f} segundos", file=arquivo_log) # Imprime no log o tempo de execução











# Fechar arquivo txt
arquivo_log.close()