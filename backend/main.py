import uvicorn
if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8888, reload=True)

from dotenv import load_dotenv

load_dotenv()

import os

# # Copy paste below where i need it, cant start it here because of uvicorn reasons
# import debugpy

# if os.getenv("DEBUG") == "1":
#     import debugpy
#     debugpy.listen(("localhost", 5678))
#     debugpy.wait_for_client()

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set

os.environ['DSP_CACHEDIR'] = os.path.join(os.getcwd(), 'cache')
os.environ['DSP_NOTEBOOK_CACHEDIR'] = os.environ['DSP_CACHEDIR']

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gradio as gr

from app.dspy_models_config import gpt3_turbo

# --- build stuff here before moving to modules ---

# --- end of build area ---

from app.simple_dspy_ui.main_ui import MainUi
gui = MainUi(target_model=gpt3_turbo, optimizer_model=gpt3_turbo).create_ui()
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

