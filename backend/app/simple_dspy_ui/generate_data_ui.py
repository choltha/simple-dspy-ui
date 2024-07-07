import gradio as gr
from app.dspy_programs.simple_copro_optimizer import CoproOptimizer

# from app.dspy_programs.simple_optimizer import optimize_prompt

class GenerateDataUi:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model
        self.copro = CoproOptimizer(target_model, optimizer_model)

    def optimize_prompt(self, signature, example_task1_input, example_task1_gold_result):
        return self.copro.optimize_prompt(signature, example_task1_input, example_task1_gold_result)

        """
        UPDATE: Damn, this is copro, as we dont have fewshots right here ... maybe make the user put in 5 examples, 2 for fewshot, 3 for test
        create new dspy program / runner
        (maybe as background task? Unclear in regards to blocking the main thread and queuing  and so on)
        add user defined signature
        fewshot-bootstrap, for X iteration (do we need a field for X, maybe just 5 for now)
        for now, use the one example by the user as TEST "set"
        then show program which got best optimisation
        """

    def test_prompt(self, optimized_prompt, test_input_context):
        return self.target_model(optimized_prompt + test_input_context)
    
    def fill_demo_inputs(self):
        return self.SIGNATURE_PLACEHOLDER, self.EXAMPLE_TASK1_INPUT_PLACEHOLDER, self.EXAMPLE_TASK1_GOLD_RESULT_PLACEHOLDER

    SIGNATURE_PLACEHOLDER = "voicerecordings transcript -> todo items"
    EXAMPLE_TASK1_INPUT_PLACEHOLDER = "So I want to create that app using DSPy to optimize my prompts. A yes, thanks for the coffe. Ok now I am going to the office an start to work. Whoa, what an idiot, almost drove me over. Ah, damn, almost forgot I want to meet with joe tomorrow."
    EXAMPLE_TASK1_GOLD_RESULT_PLACEHOLDER = "- [ ] Create an app (use DSPy for prompt optimisation)\n- [ ] Meet with Joe tomorrow"

    def create_ui(self):
        with gr.Blocks() as gui:
            with gr.Row():
                gr.Markdown("## Use this tab to generate data for your problem, if you have none.")
                demo_button = gr.Button("Apply placeholder text as demo input into all fields.")
            with gr.Row():
                signature = gr.Textbox(label="A meta description of what your task is. Can be very concise.", placeholder=self.SIGNATURE_PLACEHOLDER)
            gr.Markdown("A good example is worth 100 words of description.")
            with gr.Row():
                example_task1_input = gr.Textbox(label="Example input context", placeholder=self.EXAMPLE_TASK1_INPUT_PLACEHOLDER)
                example_task1_gold_result = gr.Textbox(label="Example golden output (ideal answer for the task with the provided context)", placeholder=self.EXAMPLE_TASK1_GOLD_RESULT_PLACEHOLDER)
            optimize_button = gr.Button("Find optimized prompt. ### TODO WE CAN USE COPRO HERE FOR MOST SIMPLE APPROACH OR NEED MORE EXAMPLES AND GO STRAIGHT TO MIPROv2!!")
            gr.Markdown("Metrics are important in DSPy, in this case we just use F1 to compare the generated text with the golden answer which essentially scores best if the text generated contains the expected text but nothing more.")
            gr.Markdown("DSPy uses fewshot learning to optimize your results")
            with gr.Row():
                optimized_prompt = gr.Textbox(label="Optimized prompt with fewshot result", interactive=False)
            gr.Markdown("Test your optimized prompt")
            with gr.Row():
                test_input_context = gr.Textbox(label="Test prompt context", placeholder="A short story about becoming a butterfly.")
                test_output = gr.Textbox(label="Test prompt result", interactive=False)
            test_button = gr.Button("Generate Test result")
            demo_button.click(fn=self.fill_demo_inputs, outputs=[signature, example_task1_input, example_task1_gold_result])
            test_button.click(fn=self.test_prompt, inputs=[optimized_prompt, test_input_context], outputs=test_output)
            optimize_button.click(fn=self.optimize_prompt, inputs=[signature, example_task1_input, example_task1_gold_result], outputs=optimized_prompt)
        return gui
