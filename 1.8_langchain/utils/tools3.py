#tools in here
from langchain_core.tools import tool

@tool
def get_module_deadline(module_name:str)->str:
 """Look up the submission deadline for a named bootcamp module.

 Args:
  module_name: The module name, such as ANN, CNN, or RNN.
 """
 deadlines = {
  "ANN":"2026-06-30",
  "CNN":"2026-07-15",
  "RNN":"2026-08-01"
 } 
 return deadlines.get(module_name, "Module not found")

@tool
def count_students_in_module(module_name:str)->str:
     """Look up how many students are enrolled in a bootcamp module."""
     counts = {
         "ANN": 60,
         "CNN": 95,
         "RNN": 120
     }
     return counts.get(module_name, "Module not found")
    

@tool
def prerequisite_counter(module_name: str) -> str:
     """Look up which module must be completed before the named module."""

     counter = {
          "ANN": "No prerequisite",
          "CNN": "ANN",
          "RNN": "CNN"
     }
     return counter.get(module_name, "Module not found")
  


@tool
def session_module_lookup(module_name:str)->str:
     """Look up the room and session schedule for a named module."""

     lookup = {
          "ANN": "Room A, Monday at 09:00",
          "CNN": "Room B, Wednesday at 11:00",
          "RNN": "Room C, Friday at 14:00"
     }
     return lookup.get(module_name, "Module not found")