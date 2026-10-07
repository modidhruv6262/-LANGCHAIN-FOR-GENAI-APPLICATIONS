from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["team"],
    template="Why do you support {team} in IPL?"
)

formatted_prompt = prompt_template.format(team="Gujarat Titans")
print(formatted_prompt)
