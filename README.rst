Configuração do Ambiente do Projeto
************************************
Programa destinado a extração de tabelas de processo de arquivos PDF através da biblioteca tabula.

Dependências
=============
* Python 3.7+

  - $ python --version
* MongoDB

  - $ mongod --version
* Java 8+

  - $ java --version

Procedimento de setup
======================
#. Instalar dependências do Python:

    * $ ./install.sh

      * se necessário habilite o arquivo com $ chmod +x install.sh

#. Ativar ambiente virtual:

    * $ source venv/bin/activate

#. Subir instância do MongoDB:

    * $ mongod

Utilização
***********
* Colocar os documentos a serem processados na pasta /documents
* $ python run.py

Resultados
***********
Ao rodar o programa o mesmo mostrará os resultados da extração como o exemplo abaixo:

- file1.pdf -

- file2.pdf ERROR

- file3.pdf OK

- file4.pdf OK

- file5.pdf OK
