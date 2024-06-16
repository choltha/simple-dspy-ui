"""Streamlit app for simple DSPy UI."""


import logging

import streamlit as st
import streamlit.components.v1 as components


logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

def optimize_prompt(signature, example_task1_input, example_task1_gold_result):
    st.session_state.optimized_prompt = f"optimized prompt dummy - signature: {signature}, example_task1_input: {example_task1_input}, example_task1_gold_result: {example_task1_gold_result}"

# basic config
st.set_page_config(page_title="Simple DSPy UI", page_icon="🤖")
if "openai_key" not in st.session_state:
    st.session_state.openai_key = ""
if "target_model" not in st.session_state:
    st.session_state.target_model = "gpt-3.5-turbo"
if "prompting_model" not in st.session_state:
    st.session_state.prompting_model = "gpt-4o"

if "signature" not in st.session_state:
    st.session_state.signature = ""

#hardcode for first prototype iteration
if "error_message" not in st.session_state:
    st.session_state.error_message = ""

if "optimized_prompt" not in st.session_state:
    st.session_state.optimized_prompt = ""

# run
st.title("Optimize prompts with DSPy")
st.markdown(
    "This prototype uses DSPy to generates an optimized prompt for a given task."
)

openai_key = st.text_input(label="OpenAI API key", placeholder="sk-something")
signature = st.text_input(
    label="A meta description of what your task is. Can be very concise.",
    placeholder="Prompt -> flash-fiction",
)
example_task1_input = st.text_area(label="Example Task 1 Input", value="A short story about a frog who jumps on a log.")
example_task1_gold_result = st.text_area(label="Example Task 1 Gold Result", value="The frog jumps on the log, slips and lands on the ground.")

st.button(
        label="Optimize prompt",
        type="primary",
        on_click=optimize_prompt,
        args=(signature, example_task1_input, example_task1_gold_result),
    )

if st.session_state.optimized_prompt:
    st.markdown("""---""")
    st.text_area(label="Optimized prompt", value=st.session_state.optimized_prompt)