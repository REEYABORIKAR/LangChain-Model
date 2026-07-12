from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='user_data.csv')
data=loader.load()
print(data[0])
print(len(data))