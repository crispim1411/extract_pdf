import os
from crawler.get_content import extract_content
from crawler.mongo_connect import DBConnect


db = DBConnect()
docs_inserted = 0

os.chdir('documents')
filenames = [file for file in os.listdir() if file.endswith('.pdf')]
for filename in filenames:
    try:
        process, docs = extract_content(filename)
        if docs and db.count({'Processo': process}) == 0:
            inserted = db.insert_many(docs)
            docs_inserted += len(inserted.inserted_ids)
            if docs_inserted:
                print(f"{filename} OK | {len(inserted.inserted_ids)} documentos")
        else:
            print(f"{filename} -")
    except:
        print(f"{filename} ERROR")

print(f"{docs_inserted} documentos inseridos na base de dados MongoDB.")
