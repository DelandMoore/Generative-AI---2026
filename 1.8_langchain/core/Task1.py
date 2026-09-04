from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = create_model(QWEN)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You area professional bootcamp announcement writer"),
    ("human","write a {tone} assignment for the following audience {audience} \n"
     "Here are the details of the bootcamp: \n{announcement_details}\n"
     "Make sure the tone matches {tone}  and the content is clear")
])

chain = prompt | model | parser

audience = "undergraduate computer science students"
details = (
    "SEED Bootcamp: 12 weeks intensive on Genai.\n"
    "starts June 17, 2026. Covers ML,DL, ANN, LLMs, Langchain"
    "includes real world projects"
)

tones = ["formal", "friendly", "urgent"]

# 3 invoke calls
for tone in tones:
    print(f"TONE: {tone.upper()}")
    result = chain.invoke({
        "audience": audience,
        "tone": tone,
        "announcement_details": details
    })
    
    print(result)
    
    
# One stream call
print("STREAMING: TONE = INSPIRATIONAL")

stream_input = {
    "audience": audience,
    "tone": "inspirational",
    "announcement_details": details
    
}

print("Streaming output token by token: \n")

for chunk in chain.stream(stream_input):
    print(chunk, end ="", flush=True)
