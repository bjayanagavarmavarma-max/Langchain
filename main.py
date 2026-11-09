from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()


def main():
    print("Hello from langchain!")
    information="""
                Gandhi redirects here. For other uses, see Gandhi (disambiguation).
                    Mohandas Karamchand Gandhi[c] (2 October 1869 – 30 January 1948) was an Indian lawyer,[2] anti-colonial nationalist,[3] and political ethicist[4] who employed nonviolent resistance to lead the successful campaign for India's independence from British rule,[5] and whose legacy would later inspire movements for civil rights and freedom across the world. The honorific Mahātmā (Sanskrit: "great-souled", "venerable"), first applied to him in 1914 in South Africa, is now used throughout the world.[6][7]
                    Born and raised in a Hindu family in coastal Gujarat, Gandhi was trained in the law at the Inner Temple in London and was called to the bar at the age of 22. After two uncertain years in India, where he was unable to start a successful law practice, Gandhi moved to South Africa in 1893 to represent an Indian merchant in a lawsuit. He went on to live in South Africa for the next 21 years. Here, Gandhi raised a family and first employed nonviolent resistance in a campaign for civil rights. In 1915, aged 45, he returned to India and soon set about organising peasants, farmers, and urban labourers to protest against discrimination and excessive land tax.
                """
    # creation of Prompt template:
    summary_template=""" given the information {information} about a person I want you to create: 1. A short summary2. two interesting facts about them"""
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm= ChatGoogleGenerativeAI(model="gemini-3.5-flash",api_key=os.environ["GEMINI_API_KEY"])
    chain= summary_prompt_template | llm # runnable interface object
    response=chain.invoke(input={"information":information}) 
    print(response.content)
    
    
    

if __name__ == "__main__":

    main()
