import gradio as gr
from app.simple_dspy_ui.simple_dspy_tutorial import SimpleDspyTutorial

class MainUi:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model

    def create_ui(self):
        simple_dspy_tutorial = SimpleDspyTutorial(self.target_model, self.optimizer_model)
        with gr.Blocks() as ui:
            gr.Markdown("# DSPy, simple.")
            with gr.Blocks():
                with gr.Tab("Tutorial"):
                    simple_dspy_tutorial.create_ui()
                with gr.Tab("Bring your own problem & data"):
                    gr.Markdown("DSPy is like machine learning for prompts. It needs a lot of data. To get you started, there is this first tab to generate data for your problem which you can then use on the 2nd Tab to actually apply DSPy to your problem and get an optimized prompt.")
                    gr.Markdown("## TODO TWO TABS HERE, again.")
                    gr.Markdown("## Use this tab to generate data for your problem, if you have none.")
                    
        return ui