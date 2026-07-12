from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template='Answer the following Question \n {question} from the following- \n {text}',
    input_variables=['question', 'text']
)

parser=StrOutputParser()
url="https://www.amazon.in/iPhone-Pro-512-Promotion-Breakthrough/dp/B0FQF5DG3P/ref=sr_1_1_sspa?crid=2XQWO68E9E98D&dib=eyJ2IjoiMSJ9.1mRTXhwxQF1jEfGnEvFdhqf6uUZx5sMbe9H5Url876eIwcK4hjBFKrzpvBUgStbFWQHBKabfkJYIaWpYrj783NWcrC68OjLOnTbHW200a9RbVtTtjQhUHnFDHEFZpnUYOQamIzEnYcTBb6I1l3Q7Q1XwYW8XjQpPK1pJXenMOxtMIU5jwa0253JyojrbBmDeD2dTRrtO8vuEhd8LvKc1QFsk610UxpFus9PBKlaxK-M.BxvikkXLVciPhWMmTHRZj3dCO8ad17142FKlqy2-IoY&dib_tag=se&keywords=iphone%2B17&qid=1775151769&sprefix=iphn%2Caps%2C378&sr=8-1-spons&aref=4YVN9ZDqCq&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
loader=WebBaseLoader(url)

docs=loader.load()

chain =prompt | model | parser

print(chain.invoke({'question':'What is the product that we are talking about?','text':docs[0].page_content}))