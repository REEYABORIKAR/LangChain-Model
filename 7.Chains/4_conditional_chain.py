# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# model1=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model1=model = ChatGroq(model='llama-3.1-8b-instant',temperature=1.8)
parser= StrOutputParser()

class FeedaBack(BaseModel):
    sentiment: Literal['positive','negative']=Field(description='Give the sentiment of thr feedback')

parser2=PydanticOutputParser(pydantic_object=FeedaBack)

prompt1= PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifire_chain=prompt1 |model1 | parser2

# result=classifire_chain.invoke({'feedback':'This ia a terrible smartphone'})
# result1=classifire_chain.invoke({'feedback':'This ia a wonderful smartphone'}).sentiment
# print(result)
# print(result1)

prompt2=PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment =='positive', prompt2 | model1 | parser),
    (lambda x:x.sentiment =='negative', prompt3 | model1 | parser),
    RunnableLambda(lambda x: "could not find sentiment") 
)
chain=classifire_chain | branch_chain
result=chain.invoke({'feedback':"This is a terrible smartphone"})
print(result)

chain.get_graph().print_ascii()
