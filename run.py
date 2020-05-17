import os
from crawler.get_content import extract_content
from crawler.mongo_connect import DBConnect
#from model.data_formater import extract_info

url = 'http://www.pdf995.com/samples/pdf.pdf'
# filename = download_file(url)
db = DBConnect()
os.chdir('documents')
filenames = [file for file in os.listdir() if file.endswith('.pdf')]
for filename in filenames:
    docs = extract_content(filename)

    # salvando no banco
    db.insert_many(docs)
db.find_all()
