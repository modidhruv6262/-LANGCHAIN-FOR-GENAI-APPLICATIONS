### 2. Problems with Direct API Approach (Why LangChain is Better)

*(Note: Although we used LangChain above as requested, if we had used the direct API approach via raw HTTP requests, we would face these issues:)*

1. **No Prompt Management:** Hardcoding prompts into JSON payloads is messy and doesn't allow for easy dynamic variable injection without massive Python string formatting.
2. **Error Handling & Parsing:** Parsing deep nested JSON response trees manually every time is highly prone to `KeyError` crashes if the API randomly changes its format or errors out.
