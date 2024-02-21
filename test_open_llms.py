import langchain
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")
llm("The first man on the moon was ...")