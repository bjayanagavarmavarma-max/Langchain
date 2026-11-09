from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent # function
from langchain_core import tools #decorator
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel,Field

class Source(BaseModel):
    """Scheme for the source of the job posting"""
    url: str = Field(..., description="URL of the job posting")

class JobPosting(BaseModel):
    """Scheme for a job posting"""
    title: str = Field(..., description="Title of the job posting")
    company: str = Field(..., description="Company offering the job")
    location: str = Field(..., description="Location of the job")
    sources: List[Source] = Field(..., description="List of sources for the job posting")

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
tools=[TavilySearch()]
#now create the agent: agent need llm and tools
agent=create_agent(model=llm,tools=tools,response_format=JobPosting)
    
def main():
    print("Hello from langchain!.....")
    query="Give me the three AI engineer Job Posting companies in Banglore for 3 to 4 years of experiences"
    result=agent.invoke({"messages":[HumanMessage(content=query)]})
    print("done searching..... check in langsmith")

if __name__ == "__main__":
    main()


"""
1. create the function of search and give tool as decorator and create the tavily search
2. create the agent that need llm and tools
3. In main function, run the query to agent
4. Structured output , to tell llm to give the output in the format of Pydantic model, so that we can use it in our application
"""