from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

## schema
class Review(BaseModel):
    key_themes:list[str]=Field(description="Write down all the key themes discussed in the review in a list")
    summary:str=Field(description="A brief summary of thr review")
    sentiment:Literal["pos","neg"]=Field(description="Return sentiment of the review either negative, positive or neutral")
    pros:Optional[list[str]]=Field(default=None, description="Write down all the pros inside a list")
    cons:Optional[list[str]]=Field(default=None, description="Write down all the cons inside a list")
    name:Optional[str]=Field(default=None, description="Name of the person who wrote the review")
   

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""
I recentaly ugraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everthing lighting fast-whether I'm gaming, multitasking, or editing photos. The 500mAh battery easily lasts a full day even with the heavy use, andt the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me awy is the 200Mp camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality
However, the weight and size make it bit uncomfortable for one-handed use. Also, Samsumg's One UI still comes with bloatware-why di I need five different Samsung apps for thuings Google already provies? The $1,300 price tag is also a hard pill to swallow
Pros:
Instanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capibilities
Long battery life withfast charging
S-Pen support is unique and useful
Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive comapred to competitors
                               
Reviewed by Reeya Borikar""")

print(result.name)
# print(result['summary'])
# print(result['sentiment'])