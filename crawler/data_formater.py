class DataFormater:
    docs = []

    @classmethod
    def add_doc(cls, process, item_number, start_period, end_period, quantity, description, tp):
        cls.docs.append({
        'Processo': process,
        'Número do item': item_number,
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
