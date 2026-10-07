### 5. ChatGPT Prompt Template Suggestion

**My Prompt to ChatGPT:**
> *"Write a system prompt template that explicitly instructs a LangChain agent on when it should use its attached Calculator tool versus when it should just answer conversationally."*

**ChatGPT's Suggestion:**
> *"You are a highly intelligent assistant. If the user asks a mathematical calculation, you MUST use the Calculator tool. If the user asks a general question (like 'Hello' or 'How are you?'), answer normally without using the tool."*

**Implementation:**
I implemented this exact string as the `system_prompt` in `task5_smart_routing.py`. The agent now perfectly routes normal conversational messages (like greetings) natively via the LLM, and successfully redirects complex math queries straight to the Python evaluation tool.
