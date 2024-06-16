from dotenv import load_dotenv

load_dotenv()

import logging
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gradio as gr

from app.simple_dspy_ui.ui import gradio_interface

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

app = gr.mount_gradio_app(app, gradio_interface, path="/")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)