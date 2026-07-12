from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
st.header('Research Tool')
# user_input=st.text_input('Enter your prompt')

paper_input=st.selectbox("Select Research Paper Name",["Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])
style_input= st.selectbox("Select Explantion Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])
length_input=st.selectbox("Select Explantion Length",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Large (detailed explanation)"])

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template=load_prompt('template.json')


# ## Fill the placeholder
# prompt=template.invoke({
# 'paper_input':paper_input,
# 'style_input':style_input,
# 'length_input':length_input
# })


if st.button('Summarize'):
    # result=model.invoke(user_input)
    # st.write(result.content)
    # st.write("Hello")

    chain=template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    # result=model.invoke(prompt)
    st.write(result.content)