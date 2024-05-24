import json
import os
import csv
import mysql.connector
from mysql.connector import errorcode
import sys
import logging

def checkPythonVersion():
    if sys.version_info < (3, 0):
        print("Este script requer Python 3 ou superior. Por favor, atualize sua versão do Python.")
        sys.exit(1)

def getConnection(params):
    try:
        connection = mysql.connector.connect(
            user=params['user'],
            password=params['password'],
            host=params['host'],
            database=params['database']
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erro ao conectar. Usuario ou senha inválidos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("O banco de dados não existe.")
        else:
            print(err)
        return None

def getTableColumns(db, table_name):
    db.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = db.fetchall()
    return [col[0] for col in columns], [col[1] for col in columns]

def validateFormatValue(value, col_type):
    if value == "\\N":
        return 'NULL'
    else:
        return f"'{value}'"
    """
    try:
        if 'int' in col_type:
            return int(value)
        elif 'float' in col_type or 'double' in col_type:
            return float(value)
        elif 'char' in col_type or 'text' in col_type or 'varchar' in col_type:
            return f"'{value}'"
        elif 'date' in col_type:
            return f"'{value}'"
        else:
            return f"'{value}'"
    except ValueError:
        return 'NULL'
    """

def insertDataIntoTable(db, table_name, columns, row):
    col_names = ', '.join(columns[0])
    values = ', '.join([ validateFormatValue( value, col_type ) for value, col_type in zip(row, columns[1]) ] )
    query = f"INSERT INTO {table_name} ({col_names}) VALUES ({values})"
    db.execute(query)

def main():
    checkPythonVersion()

    # LOG de erros
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

    # Carregando os paramentros do arquivo json
    with open('py-csv2mysql.json', 'r') as f:
        config = json.load(f)

    # Conectando a base de dados
    conn = getConnection(config)
    if conn is None:
        return
    
    db = conn.cursor()

    # Processando cada arquivo .CSV existente no diretório informado no arquivo json
    for csv_filename in os.listdir(config['csv_directory']):
        if csv_filename.endswith('.csv'):
            table_name = os.path.splitext(csv_filename)[0]
            csv_path = os.path.join(config['csv_directory'], csv_filename)
            print(f"Importando {csv_path} para a tabela {table_name}...")

            try:
                with open(csv_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=config['delimiter'])

                    # Caso a primeira linha dos arquivos contenha as colunas
                    # o parametro 'skip_header' deverá ser setado como true
                    if config['skip_header']:
                        next(csv_reader)

                    # Capturando as colunas da tabela atual
                    columns = getTableColumns(db, table_name)

                    for row in csv_reader:
                        insertDataIntoTable(db, table_name, columns, row)
            except Exception as e:
                logging.error(f"Erro ao processar o arquivo {csv_path}: {e}")

    conn.commit()
    db.close()
    conn.close()

if __name__ == "__main__":
    main()

