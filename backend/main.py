from dotenv import load_dotenv

load_dotenv()

import os
import debugpy

if os.getenv("DEBUG") == "1":
    import debugpy
    debugpy.listen(("localhost", 5678))
    debugpy.wait_for_client()

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set

os.environ['DSP_CACHEDIR'] = os.path.join(os.getcwd(), 'cache')
os.environ['DSP_NOTEBOOK_CACHEDIR'] = os.environ['DSP_CACHEDIR']

import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gradio as gr

# --- build stuff here before moving to modules ---

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

# --- end of build area ---

from app.simple_dspy_ui.ui import SimpleDSPyUI
gui = SimpleDSPyUI(target_model=gpt_turbo, optimizer_model=gpt_turbo).create_ui()
app = FastAPI(title="Simple DSPy UI")

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set

if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app = gr.mount_gradio_app(app, gui, path="/")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)