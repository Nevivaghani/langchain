from langchain.chains import ConversationChain
import langchain_helper as hp

convo = ConversationChain(llm = hp.llm)

print(convo.run("what is 5 + 5?"))
print(convo.run("who was captain of the enterprise?"))
print(convo.prompt.template)
print(convo.memory.buffer)
