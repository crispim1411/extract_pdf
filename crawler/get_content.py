import os
import wget
from PyPDF2 import PdfFileReader as pdf_read


def download_file(url):
    """Baixa e salva arquivo a partir de sua url"""
    filename = url.split('/')[-1]
    if filename not in os.listdir():
        filename = wget.download(url)
    return filename


def extract_content(filename):
    """Extrai metadados e conteúdo de um arquivo PDF"""
    with open(filename, 'rb') as file:
        pdf = pdf_read(file)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        content = []
        for page in pdf.pages:
            content.append(page.extractText())

        metadata = f"""
        Information about {filename}:

        Author: {info.author}
        Creator: {info.creator}
        Producer: {info.producer}
        Subject: {info.subject}
        Title: {info.title}
        Number of pages: {number_of_pages}
        """
    return metadata, content
