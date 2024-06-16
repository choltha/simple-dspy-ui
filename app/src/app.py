from dotenv import load_dotenv

load_dotenv()


import debugpy

if os.getenv("DEBUG") == "1":
    import debugpy
    debugpy.listen(("localhost", 5678))
    debugpy.wait_for_client()


import gradio as gr

def greet(name):
    return "Hello " + name + "!"

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)