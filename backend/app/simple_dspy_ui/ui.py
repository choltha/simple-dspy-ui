import gradio as gr

def optimize_prompt(signature, example_task1_input, example_task1_gold_result):
    return f"optimized prompt dummy - signature: {signature}, example_task1_input: {example_task1_input}, example_task1_gold_result: {example_task1_gold_result}"

def test_prompt(optimized_prompt, test_input_context):
    return f"test prompt dummy - optimized_prompt: {optimized_prompt}, test_input_context: {test_input_context}"

with gr.Blocks() as gui:
    gr.Markdown("## Simply optimize your prompts!")
    with gr.Row():
        signature = gr.Textbox(label="A meta description of what your task is. Can be very concise.", placeholder="Prompt -> Flash Fiction")
    gr.Markdown("A good example is worth 100 words of description.")
    with gr.Row():
        example_task1_input = gr.Textbox(label="Example input context", placeholder="A short story about a frog who jumps on a log.")
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
    test_button.click(fn=test_prompt, inputs=[optimized_prompt, test_input_context], outputs=test_output)
    optimize_button.click(fn=optimize_prompt, inputs=[signature, example_task1_input, example_task1_gold_result], outputs=optimized_prompt)
