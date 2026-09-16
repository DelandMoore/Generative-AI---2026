from langchain.agents import create_agent
from .models import create_model
from utils.tools3 import get_module_deadline, count_students_in_module,prerequisite_counter,session_module_lookup

model = create_model()

agent = create_agent(
    model = "anthropic:claude-sonnet-5",
    tools = [get_module_deadline, count_students_in_module,prerequisite_counter,session_module_lookup],
    system_prompt="Can a student who hasn't finished ANN start CNN, and how many students are already in CNN?"
)

result = agent.invoke({"message": [{"role": "user", "content": " Can a student who hasn't finished ANN start CNN, and how many students are already in CNN?"}]})
print(result["messages"][-1].content)