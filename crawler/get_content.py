from tabula import read_pdf
from crawler.data_formater import DataFormater


def extract_content(filename):
    """Extrai metadados e conteúdo de um arquivo PDF"""
    try:
        data = read_pdf(filename, lattice=True, pages='all')

        basic_data = None
        items_data = []
        for table in data:
            if len(table) == 10 and basic_data is None:
                basic_data = table
            elif len(table) == 4:
                items_data.append(table)

        process_number = basic_data.loc[basic_data.get('Unnamed: 0') == 'ID da Oportunidade']['Unnamed: 1'].item()
        start_period = basic_data.loc[basic_data.get('Unnamed: 0') == 'Início do período de cotação']['Unnamed: 1'].item()
        end_period = basic_data.loc[basic_data.get('Unnamed: 0') == 'Fim do período de cotação']['Unnamed: 1'].item()

        documents = []
        for item in items_data:
            quantity = item.loc[1]['Unnamed: 2']
            description = item.loc[2][1]
            tp = item.loc[3][1].split('Tp:')[-1].split('\r')[0].strip()
            DataFormater.add_doc(process_number, start_period, end_period, quantity, description, tp)
        docs = DataFormater.get_docs()
        DataFormater.clear()
        return docs

    except Exception as e:
        raise e
