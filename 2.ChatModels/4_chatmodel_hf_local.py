# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEndpoint

# # llm=HuggingFacePipeline.from_model_id(
# #     model_id="unsloth/Llama-3.2-3B-Instruct",
# #     task='text-generation',
# #     # pipeline_kwargs=dict(temperature=0.5, max_new_tokens=100)
# #     )
# llm=HuggingFaceEndpoint(
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation"
# )
# model=ChatHuggingFace(llm=llm)
# result= model.invoke("What is the capital of India")
# print(result.content)



import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# 1. Set your token (ensure it's the full string from your screenshot)
hf_token = "hf_...your_full_token_here..." 

# 2. Configure the Endpoint
# Note: We move max_new_tokens outside of pipeline_kwargs 
# to avoid the "unexpected keyword argument" error.
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct", # This is NOT gated
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=100
)

# 3. Wrap in ChatHuggingFace
model = ChatHuggingFace(llm=llm)

try:
    # 4. Invoke
    result = model.invoke("What is the capital of India?")
    print(result.content)
except Exception as e:
    # If this still says 401, you likely haven't clicked "Access" on the Meta-Llama page
    print(f"Error: {e}")