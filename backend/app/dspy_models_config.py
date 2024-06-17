import dspy
import os

# @todo move to backends, maybe use dspy dev-branch instead?
api_key = os.getenv("API_KEY_OPENAI")
gpt_turbo = dspy.OpenAI(
    model = 'gpt-3.5-turbo', 
    api_key = api_key, 
    model_type='chat',
    temperature=0.0,
    max_tokens=1000
)