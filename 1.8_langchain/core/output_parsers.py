from pydantic import BaseModel, Field
from .models import create_model
from config import QWEN
model = create_model()

# create the blueprint for the output parser
class Player(BaseModel):
    name: str = Field(description="The name of the football player")
    age: int = Field(description="The age of the football player")
    club: str = Field(description="The club the football player currently plays for")
    nationality: str = Field(description="The nationality of the football player")
    national_flag: str = Field(description="The national flag of the football player's country as an emoji")

class TopTen(BaseModel):
    opinion: str = Field(description="A brief opinion about the top ten football players")
    players: list[Player] = Field(description="A list of the top ten football players")
structured_model = model.with_structured_output(TopTen)
results = structured_model.invoke("who won the fifa balon d'or in 2025")
# .model_Dump( ) will return the output in a dictionary format
print(results.model_dump())
#print(f'the player\'s name is {results.name}, he is {results.age} years old, he plays for {results.club}')

    