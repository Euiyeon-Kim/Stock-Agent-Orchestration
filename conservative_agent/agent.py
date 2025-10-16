from dotenv import load_dotenv
from google.adk.agents import LlmAgent

from .prompt import INSTRUCTION
from .tools import TOOLS

load_dotenv()

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='conservative_investment_agent',
    description="Conservative investment advisor",
    instruction=INSTRUCTION,
    tools=TOOLS,
)
