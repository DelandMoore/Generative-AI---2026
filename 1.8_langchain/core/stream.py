from .models import create_model
from config import QWEN

model = create_model(QWEN)
response = model.invoke("who is the first lady of the united state of America")
print(response.content)


# for chunk in model.stream("Who is the GOAT of football?" ):
#     print(f"{chunk.content}", end="", flush=True)

message_batch = [
    "why do they call black Americans Nigros",
    "Who was the first president of Cameroon",
    "who started world war 2?"
]
responses = model.batch(message_batch)
for r in responses:
    print(r.text)