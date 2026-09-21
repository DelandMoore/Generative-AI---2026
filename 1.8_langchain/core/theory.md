## Part A: Theoretical Exercises

### A1. Taxonomy of Agents

A shallow agent, such as a basic ReAct agent, usually follows a short loop: receive a request, choose a tool, observe the result, and produce an answer. Its reasoning and intermediate results mostly remain inside the current conversation context.

A Deep Agent is designed for larger, longer-running tasks. It adds explicit planning, a persistent file system, sub-agent delegation, and stronger state and context management. Instead of keeping every result in the prompt, it can save large outputs to files and read them again only when needed.

The main architectural differences are:

- A planning or todo-list tool for breaking work into steps.
- File-system tools for reading, writing, and managing persistent task data.
- A task or delegation tool for creating isolated sub-agents.
- A stateful graph that can route, repeat, pause, and resume work.
- Context-management middleware for handling long conversations and large results.

### A2. Decomposition Analysis

For a request such as "Organize a 10-day research trip," a Deep Agent first converts the goal into a todo list:

1. Identify the destination, dates, budget, and research objectives.
2. Research transportation and entry requirements.
3. Find accommodation near the relevant research locations.
4. Identify institutions, experts, or events to visit.
5. Build a day-by-day schedule.
6. Estimate costs and check the schedule against the budget.
7. Save detailed research results in files.
8. Read the saved results and produce one final itinerary.

The agent marks each item as `pending`, `in_progress`, or `done`. Independent tasks can be delegated to sub-agents, while the main agent coordinates dependencies and combines the results. Large search results are written to files instead of being kept entirely in the active context.

### A3. Memory Persistence

The file system gives a Deep Agent external, durable memory for a task. Large research results, plans, intermediate documents, and summaries can be written to named files. The agent can later read only the file or section it needs.

Standard chat history keeps previous messages in the conversation context. This is useful for continuity, but it becomes expensive and difficult to manage as the conversation grows. Every message may be replayed into later model calls, increasing prompt size and making it harder to focus on relevant information.

Therefore, file-system memory supports selective retrieval and long-running work, while ordinary chat history mainly provides sequential conversational context.

### A4. Sub-Agent Delegation

The parent agent acts as a coordinator. It divides a complex objective into smaller tasks and sends each task to a specialized sub-agent through a task tool.

For the research-trip example, separate sub-agents could investigate transportation, accommodation, research institutions, and costs. Each sub-agent works with its own isolated context, so its intermediate tool calls do not fill the parent agent's context window. It returns one distilled result to the parent agent, which checks the result, updates the plan, and combines the findings into the final answer.

This improves organization, parallelism, and context efficiency. It also allows each sub-agent to receive a focused role and instructions.

### A5. State Management

A LangGraph graph is better for maintaining agent state than a simple linear chain because an agent workflow is not always a fixed sequence. A graph can represent different nodes for the agent, tools, sub-agents, and completion, with conditional edges between them.

The graph can route to a tool when the model requests one, delegate to a sub-agent when a task requires specialization, loop back after an observation, retry a failed step, or finish when the work is complete. State is carried between nodes, so messages, todo items, tool results, and progress status remain available throughout the workflow.

A linear LCEL chain normally runs Step 1, then Step 2, then Step 3, and finally returns an output. It is simple and predictable, but it does not naturally support branching, loops, retries, delegation, or resuming from an intermediate state. LangGraph's stateful graph structure is therefore more suitable for complex Deep Agent workflows.