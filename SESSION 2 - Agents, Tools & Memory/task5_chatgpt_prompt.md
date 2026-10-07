### 5. Using ChatGPT to Generate a Combined Agent

**My Prompt to ChatGPT:**
> *"Write a Python script using LangChain that combines a custom Search tool and a Calculator tool. Make the domain focused on Food Delivery so it can look up restaurant prices and calculate the total bill."*

**Modifications Made to ChatGPT's Output:**
1. **Agent Architecture:** ChatGPT suggested the heavily deprecated `initialize_agent` with old tool schemas. I modernized it using LangChain 1.4.3's powerful `create_agent` framework which natively supports graph-based state and tool invocation loops without rigid legacy classes.
2. **Simplified Tools:** Instead of wrestling with boilerplate `Tool.from_function` definitions, `create_agent` automatically introspects raw Python functions using their type hints and docstrings.
3. **Math Safety:** ChatGPT's script used an unfiltered `eval()` for the calculator tool. I explicitly secured it by filtering allowed characters to prevent dangerous code execution.
