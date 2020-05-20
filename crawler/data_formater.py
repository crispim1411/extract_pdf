class DataFormater:
    docs = []

    @classmethod
    def add_doc(cls,item_number, process, start_period, end_period, quantity, description, tp):
        cls.docs.append({
        'Número do item': item_number,
        'Processo': process,
        'Inicio do período de cotação': start_period,
        'Fim do período de cotação': end_period,
        'Quantidade': quantity,
        'Descrição de item': description,
        'Tp': tp})

    @classmethod
    def get_docs(cls):
        return cls.docs

    @classmethod
    def clear(cls):
        cls.docs = []
