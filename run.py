import os
from crawler.get_content import extract_content
from crawler.mongo_connect import DBConnect


db = DBConnect()
os.chdir('documents')
filenames = [file for file in os.listdir() if file.endswith('.pdf')]
for filename in filenames:
    docs = extract_content(filename)

    # salvando no banco
    if db.count({'Processo':docs[0]['Processo']}) == 0:
        db.insert_many(docs)
