# py-csv2mysql

Este script Python lê arquivos CSV e insere seus dados em tabelas MySQL/MariaDB. Ele é configurável através de um arquivo JSON e suporta a substituição de valores `\N` por `NULL`.

## Requisitos

- Python 3.6 ou superior
- mysql-connector-python

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/HudsonLopesMartins/py-csv2mysql.git
    cd py-csv2mysql
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install mysql-connector-python
    ```

## Configuração

Crie um arquivo `py-csv2mysql.json` no mesmo diretório do script com o seguinte conteúdo:

```json
{
    "user": "seu_usuario",
    "password": "sua_senha",
    "host": "localhost",
    "database": "nome_do_banco",
    "delimiter": ",",
    "skip_header": true,
    "csv_directory": "caminho/para/a/pasta/csv"
}
```
- user: Nome de usuário do banco de dados MySQL/MariaDB.
- password: Senha do banco de dados MySQL/MariaDB.
- host: Endereço do servidor MySQL/MariaDB (geralmente localhost).
- database: Nome do banco de dados onde os dados serão inseridos.
- delimiter: Delimitador de colunas nos arquivos CSV (por exemplo, , ou ;).
- skip_header: Define se a primeira linha dos arquivos CSV deve ser ignorada (true ou false).
- csv_directory: Caminho para a pasta onde os arquivos CSV estão localizados.


## Uso

Execute o script:

```bash
    python py-csv2mysql.py
```
O script irá ler todos os arquivos CSV no diretório especificado e inserirá os dados nas tabelas MySQL/MariaDB correspondentes. Se ocorrer algum erro durante a execução, ele será registrado no arquivo error_log.txt.


## Tratamento de Erros

Se ocorrer um erro durante a inserção de dados, o script registrará uma mensagem de erro no arquivo error_log.txt, incluindo o nome do arquivo CSV onde o erro ocorreu e a descrição do erro.


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## 🚀 Sobre mim

Programador desde 2005, com desenvolvimento de ferramentas para área comercial, gestão de arquivos e produção textil.
Com conhecimento nas linguagens e tecnologias:
- Delphi
- PHP
- Python
- Ionic/VueJS
- JQuery
- SQL (Oracle, SQL Server, MySQL, Firebird) | MongoDB
- IA

## Autor

- [@HudsonLopesMartins](https://github.com/HudsonLopesMartins)
- [Linkedin](https://www.linkedin.com/in/hudson-lopes-martins-25123119/)


## Licença

Este projeto está licenciado sob a Licença [MIT](https://choosealicense.com/licenses/mit/). Veja o arquivo LICENSE para mais detalhes.
