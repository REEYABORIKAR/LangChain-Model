from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

## create langchain for ipl players

docs1=Document(
    page_content=" Virat Kohli is one of the most successful and consistent batsmen life in a stream known for his aggressive batting style",
    metadata={'team':"Royal Challengers Banglore"}
)
docs2=Document(
    page_content=" Sharma is the most successful captain and I built history leading Mumbai Indians to fight titles he snubbed by his captaincy",
    metadata={'team':"Mumbai Indians"}
)

docs3=Document(
    page_content=" MS Dhoni famously known as a Captain Cool has meet Chennai Super Kings to multiple IPL topics his finishing skills wicket keeping",
    metadata={'team':"Chennai Super Kings"}
)

docs4=Document(
    page_content=" Jasprit numerous considered one of the best fast bowlers 2020 they were playing for Mumbai DMK is known for bowling",
    metadata={'team':"Mumbai Indians"}
)

docs5=Document(
    page_content=" Ravindra Jadeja is a dynamic all round of who contributes with both bad and ball.Represnting of Chennai Super Kings",
    metadata={'team':"Chennai Super Kings"}
)

docs=[docs1,docs2,docs3,docs4,docs5]
vectore_store=Chroma(
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"),
    persist_directory='chroma_db',
    collection_name='sample'
)

## add documents
vectore_store.add_documents(docs)

## view documents
vectore_store.get(include=['embedding','documents','metadatas'])