import gradio as gr

def greet(name):
    return "Hello " + name + "!"

gradio_interface = gr.Interface(fn=greet, inputs="text", outputs="text")