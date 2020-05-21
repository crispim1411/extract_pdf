from tabula import read_pdf
from crawler.data_formater import DataFormater


def extract_content(filename):
    """Extrai conteúdo de um arquivo PDF com base em tabela de processos específica"""
    try:
        data = read_pdf(filename, lattice=True, pages='all', pandas_options={'header':None})
        previous_item_number = 0
        for table in data:
            if table.isin(['Dados Básicos']).any(axis = None):
                process_number = table.where(table[0]=='ID da Oportunidade').dropna().values[0][1]
                start_period = table.where(table[0]=='Início do período de cotação').dropna().values[0][1]
                end_period = table.where(table[0]=='Fim do período de cotação').dropna().values[0][1]

            if table.isin(['Número\rdo item']).any(axis = None):
                item_number = int(table.loc[2].values[0])
                quantity = table.loc[2].values[3]
                description = table.loc[3].values[1]
                tp = table.loc[4].values[1].split('Tp:')[-1].split('\r')[0].strip()
                DataFormater.add_doc(process_number, item_number, start_period, end_period, quantity, description, tp)

                if item_number != (previous_item_number + 1):
                    raise Exception("Não foi possível a extraição de todos os itens.")
                previous_item_number = item_number

        docs = DataFormater.get_docs()
        DataFormater.clear()
        return process_number, docs

    except Exception as e:
        raise e
