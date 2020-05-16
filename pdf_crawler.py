import os
from crawler.get_content import extract_content, download_file
from crawler.mongo_connect import DBConnect

url = 'http://www.pdf995.com/samples/pdf.pdf'
# filename = download_file(url)
os.chdir('documents')
filenames = [file for file in os.listdir() if file.endswith('.pdf')]
for filename in filenames:
    metadata, content = extract_content(filename)

    #mostrando resultado
    print(metadata)

    # salvando no banco
    db = DBConnect()
    db.insert_one({'metadata': metadata, 'content': content})
db.find_all()
