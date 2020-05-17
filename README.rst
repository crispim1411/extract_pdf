Configuração do Ambiente do Projeto
************************************
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
* Colocar os documentos a serem processados na pasta documents.
* $ python run.py
