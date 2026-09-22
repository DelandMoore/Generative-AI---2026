#tool call here
from utils.tools3 import get_module_deadline, count_students_in_module, prerequisite_counter, session_module_lookup
from .models import create_model
from langchain_core.messages import HumanMessage, ToolMessage

tools = [get_module_deadline, count_students_in_module, prerequisite_counter, session_module_lookup]

llm = create_model().bind_tools(tools)


tools_by_name={t.name: t for t in tools}
print(tools_by_name)

def run_question(question: str) -> None:
    """Run one question through the model and any requested tools."""
    message = [HumanMessage(content=question)]
    ai_response = llm.invoke(message)
    print(f"\nQuestion: {question}")
    print(f"Tool calls: {ai_response.tool_calls}")

    if not ai_response.tool_calls:
        print(f"Answer: {ai_response.content}")
        return

    message.append(ai_response)
    for tool_call in ai_response.tool_calls:
        tool_fn = tools_by_name[tool_call["name"]]
        result = tool_fn.invoke(tool_call["args"])
        message.append(
            ToolMessage(content=str(result), tool_call_id=tool_call["id"])
        )

    final = llm.invoke(message)
    print(f"Answer: {final.content}")


questions = [
    "How many students are in the CNN module and what is its submission deadline?",
    "Which module must be completed before RNN, and where and when is the RNN session?",
    "How many students are in ANN, what is its deadline, and where is its session?",
    "What is a neural network?",
]

for question in questions:
    run_question(question)