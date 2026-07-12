from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
result=model.invoke("Write 5 line poem in cricket")
# print(result)
print(result.content)