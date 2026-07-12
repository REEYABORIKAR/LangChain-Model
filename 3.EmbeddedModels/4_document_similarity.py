from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",output_dimensionality=300)

documents=[
    "Virat Kohli — One of the greatest modern batsmen, known for his aggressive batting and long tenure as captain of the Indian national team.",
    "MS Dhoni — Legendary Indian captain and wicketkeeper-batsman who led India to the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy.",
    "Sachin Tendulkar — Widely regarded as the “God of Cricket,” he holds numerous records including the most runs in international cricket.",
    "Rohit Sharma — Indian captain famous for elegant batting and the record of three double centuries in One Day Internationals.",
    "Jasprit Bumrah — India’s premier fast bowler known for his unique action, deadly yorkers, and match-winning performances across formats."
]

query="tell me about virat kholi"
doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print('Simialrity score is: ', score)