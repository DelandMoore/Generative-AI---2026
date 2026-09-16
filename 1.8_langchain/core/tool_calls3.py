#tool call here
from utils.tools3 import get_module_deadline, count_students_in_module,prerequisite_counter,session_module_lookup
#from utils.tools import prerequisite_counter
from .models import create_model
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

tools = [get_module_deadline, count_students_in_module, prerequisite_counter, session_module_lookup]

llm = create_model().bind_tools(tools)


tools_by_name={t.name: t for t in tools}
print(tools_by_name)
message = [HumanMessage(" how many students are in the CNN module and what is the deadline for submission?")]
ai_response = llm.invoke(message)
print(ai_response)


message.append(ai_response)

for tool in ai_response.tool_calls:
    tool_fn = tools_by_name[tool["name"]]
    result=tool_fn.invoke(tool["args"])
    message.append(ToolMessage(content=str(result), tool_call_id=tool["id"]))
final=llm.invoke(message)
print(final.content)