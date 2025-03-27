# from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
import langchain_helper as hp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

memory = ConversationBufferWindowMemory(k = 1)

prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.only one name for this"
    )

chain = LLMChain(llm=hp.llm, prompt=prompt_template_name, memory = memory)
name = chain.run(cuisine="Mexican")
print(name)

# name = chain.run(cuisine="Indian")
# print(name)
print(chain.memory.buffer)