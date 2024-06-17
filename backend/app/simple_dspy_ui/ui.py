import gradio as gr

# from app.dspy_programs.simple_optimizer import optimize_prompt

class SimpleDSPyUI:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model

    def optimize_prompt(self, signature, example_task1_input, example_task1_gold_result):

        return f"optimized prompt dummy - signature: {signature}, example_task1_input: {example_task1_input}, example_task1_gold_result: {example_task1_gold_result}"
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
    
    def create_ui(self):
        with gr.Blocks() as gui:
            gr.Markdown("## Simply optimize your prompts!")
            with gr.Row():
                signature = gr.Textbox(label="A meta description of what your task is. Can be very concise.", placeholder="keywords -> Flash Fiction, 100 words max")
            gr.Markdown("A good example is worth 100 words of description.")
            with gr.Row():
                example_task1_input = gr.Textbox(label="Example input context", placeholder="frog, jump, log")
                example_task1_gold_result = gr.Textbox(label="Example golden output (what should the lm generate in the best case)", placeholder="The frog jumps on the log, slips and lands on the ground.")
            optimize_button = gr.Button("Find optimized prompt.")
            gr.Markdown("DSPy uses fewshot learning to optimize your results")
            with gr.Row():
                optimized_prompt = gr.Textbox(label="Optimized prompt with fewshot result", interactive=False)
            gr.Markdown("Test your optimized prompt")
            with gr.Row():
                test_input_context = gr.Textbox(label="Test prompt context", placeholder="A short story about becoming a butterfly.")
                test_output = gr.Textbox(label="Test prompt result", interactive=False)
            test_button = gr.Button("Generate Test result")
            test_button.click(fn=self.test_prompt, inputs=[optimized_prompt, test_input_context], outputs=test_output)
            optimize_button.click(fn=self.optimize_prompt, inputs=[signature, example_task1_input, example_task1_gold_result], outputs=optimized_prompt)
        return gui