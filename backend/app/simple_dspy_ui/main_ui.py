import gradio as gr
from app.simple_dspy_ui.generate_data_ui import GenerateDataUi

class MainUi:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model

    def create_ui(self):
        generate_data_ui = GenerateDataUi(self.target_model, self.optimizer_model)
        return gr.TabbedInterface(
            [
                generate_data_ui.create_ui(),
                gr.Markdown("DSPy placeholder"),
            ],
            ["Data Generation", "DSPy"]
        )