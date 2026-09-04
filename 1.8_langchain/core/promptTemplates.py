# get the model in and make sure it works
# from .models import create_model

# from config import  QWEN
# #We are going to be using something called ChatPromptTemplate to creat prompt template
# from langchain_core.prompts import ChatPromptTemplate 
# model = create_model(QWEN)
# # # a good example for prompt template

# # describe this (footbale_player) in one sentence
# # given this (data) about this school , answer related questions asked by the user


# prompt_template = ChatPromptTemplate.from_message(
#     [
#         # System message: "a message given to the model in order for it to determine how to respond to users"
#         # human message: "a message given by the user to the mode"
#         ("system","please in one sentence describe this {football_player} and give a brief history of his career, and also provide a list of his achievements in football."),
#         ("human", "{question}")
#     ]
# )

# football_player = input("Enter the name of the football player:")
# question = input("Enter the question you want to ask about the football player")


# chain = prompt_template | model
# result = chain.invoke({
#     "football_player": football_player,
#     "question": question
# })

# # to use this prompttemplate we use the invoke method:
# # prompt_template.invoke({
# #     "football_player": "Lionel Messi"
# #     "question": "What are the achievements of Lionel Messi in football"
# # })



from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = create_model(QWEN)
parser = StrOutputParser()

#prompt_template -> model -> convert to string

prompt = ChatPromptTemplate.from_messages([
    ("system","you are a concise teaching assistant, answer in {max_sentences} sentences"),
    ("human","{question}")
])

chain = prompt | model | parser
result = chain.invoke({
    "max_sentences": 5,
    "question": "What is the difference between  CNN and ANN?"
})

print(result)