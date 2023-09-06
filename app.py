from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain.llms import OpenAI
llm=OpenAI(model_name="text-davinci-003", temperature=0.9)
llm("Explain machine learning in one paragraph")