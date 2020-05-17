import os
from crawler.get_content import extract_content
from crawler.mongo_connect import DBConnect


db = DBConnect()
docs_inserted = 0

os.chdir('documents')
filenames = [file for file in os.listdir() if file.endswith('.pdf')]
for filename in filenames:
    try:
        docs = extract_content(filename)
        if db.count({'Processo':docs[0]['Processo']}) == 0:
            inserted = db.insert_many(docs)
            docs_inserted += len(inserted.inserted_ids)
            if docs_inserted:
                print(f"{filename} OK")
        else:
            print(f"{filename} -")
    except Exception as e:
        print(f"{filename} ERROR")

print(f"{docs_inserted} documentos inseridos na base de dados MongoDB.")
