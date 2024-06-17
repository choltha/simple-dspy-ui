import gradio as gr
from app.simple_dspy_ui.generate_data_ui import GenerateDataUi

class MainUi:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model

    def create_ui(self):
        generate_data_ui = GenerateDataUi(self.target_model, self.optimizer_model)
        with gr.Blocks() as ui:
            gr.Markdown("# DSPy")
            gr.Markdown("DSPy is like machine learning for prompts. It needs a lot of data. To get you started, there is this first tab to generate data for your problem which you can then use on the 2nd Tab to actually apply DSPy to your problem and get an optimized prompt.")
            with gr.Blocks():
                with gr.Tab("Data Generation"):
                    generate_data_ui.create_ui()
                with gr.Tab("DSPy"):
                    gr.Markdown("DSPy placeholder")
        return ui