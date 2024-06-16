from dotenv import load_dotenv

load_dotenv()

import debugpy
import os

if os.getenv("DEBUG") == "1":
    import debugpy
    debugpy.listen(("localhost", 5678))
    debugpy.wait_for_client()

import gradio as gr

from app.gradio_ui.ui import gradio_iface


app = FastAPI(title="DSPy x FastAPI")

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


app = gr.mount_gradio_app(app, gradio_iface, path="/gradio")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)