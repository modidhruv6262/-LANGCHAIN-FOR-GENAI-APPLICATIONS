import warnings
from dotenv import load_dotenv
from langchain_core.tools import Tool

warnings.filterwarnings('ignore')
load_dotenv()

def custom_calculator(expression: str) -> str:
    try:
        allowed = "0123456789+-*/(). "
        if any(c not in allowed for c in expression):
            return "Invalid characters"
        return str(eval(expression))
    except Exception as e:
        return str(e)

calc_tool = Tool(
    name="Calculator",
    func=custom_calculator,
    description="Useful for solving math questions like 'What is 15*3?'"
)

print("--- Custom Tool Class Created ---")
print(f"Tool Name: {calc_tool.name}")
print(f"Tool Description: {calc_tool.description}")

test_expr = "15*3"
print(f"Test Execution ({test_expr}):", calc_tool.invoke(test_expr))
