from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='policies',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()

for docu in docs:
    print(docu.metadata)