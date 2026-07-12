from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='llama-3.1-8b-instant',temperature=1.8)
result=model.invoke("Write 5 line poem in cricket")
# print(result)
print(result.content)