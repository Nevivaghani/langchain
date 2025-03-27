from langchain.agents import AgentType, initialize_agent, load_tools
import langchain_helper as hp

tools = load_tools(["serpapi", "llm-math"], llm=hp.llm, serpapi_api_key="serpapi_api_key")

agent = initialize_agent(
    tools,
    hp.llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

response = agent.run("what was the GDP of the US in 2022 plus 5?")