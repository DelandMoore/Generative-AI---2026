from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = create_model(QWEN)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Give a one paragraph explanation for {topic} and should be channeled to this {audience} audience"),
    ("human", "{topic}")
    
])

topic = input("Enter the topic you want to ask about: ")
audience = input("Enter the target audience: ")
chain = prompt | model | parser
result = chain.invoke({
    "topic": topic,
    "audience": audience
})
print(result)