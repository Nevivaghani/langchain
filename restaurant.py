from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import langchain_helper as hp

def generate_restaurant_name_and_items(cuisine):

    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.only one name for this"
    )

    name_chain = LLMChain(llm=hp.llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Run the chain with "Arabian" cuisine
    # response = chain.run(cuisine="Arabian")

    prompt_template_items = PromptTemplate(
        input_variables= ['restaurant_name'],
        template= """Suggest some menu for {restaurant_name} restaurant. Return it as comma separated list"""
    )

    food_items_chain = LLMChain(llm=hp.llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ["cuisine"],
        output_variables = ["restaurant_name", "menu_items"]
        )
    # response = chain.run({"cuisine": "Indian"})
    # response = chain.invoke({"cuisine": "Indian"})
    response = chain({"cuisine": cuisine})
    return response



if __name__ == '__main__':
    generate_restaurant_name_and_items('Mexican')