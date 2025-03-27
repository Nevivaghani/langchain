from langchain.agents import AgentType, initialize_agent, load_tools
import langchain_helper as hp

tools = load_tools(["wikipedia", "llm-math"], llm=hp.llm)

agent = initialize_agent(
        tools,
        hp.llm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

response = agent.run("When was Elon musk born? What is his age right now in 2025?")
print(response)