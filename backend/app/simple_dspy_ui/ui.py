import gradio as gr

def optimize_prompt(signature, example_task1_input, example_task1_gold_result):
    return f"optimized prompt dummy - signature: {signature}, example_task1_input: {example_task1_input}, example_task1_gold_result: {example_task1_gold_result}"


gradio_interface = gr.Interface(fn=optimize_prompt, inputs=["text", "text", "text"], outputs="text", flagging_options=["good", "bad"])