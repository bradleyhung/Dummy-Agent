import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct", api_key=os.getenv("HF_TOKEN"))

# Dummy function
def get_weather(location):
    return f"the weather in {location} is sunny with low temperatures. \n"

get_weather('London')

# Let's concatenate the base prompt, the completion until function execution and the result of the function as an Observation
new_prompt=get_weather('London')
print(new_prompt)