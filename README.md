# Simple DSPy Ui

## Goals
Enable everyone to profit from DSPy super prompts.

Main focus should be ease of use.

Maximum transparency:
- Simple wording, tooltips for advanced explainations / DSPy wording
- Show progress (diff view betweeen steps?)

Explainer, that DSPy is basically machinelearning applied to prompts and needs examples for train/test.
Add tooling to generate exactly such initial data to get the DSPy flywheel going.

## Sections / Tabs
1. Data generation. Not really DSPy but a loop to get some basic data going.
2. DSPy Tab, use data generated on 1st Tab to run the actual DSPy experiments.

## How to run
- Install pdm if not installed yet
- `cd backend`
- `pdm install`
- `pdm run main.py`

## Techstack
- dspy
- gradio for max prototyping speed

## Credits
- DSPy is the backbone of this project

## Thinks to keep in Mind
Avoid putting it on rails too much, magic comes from end-to-end AI experimentation!

## Ideas

### Examples
Currently I use short stories, but i think logic puzzles are way more fun!

### Hardware
- Try to get it running with phi3 mini 4k (or 128k?) to run on a zero space on HF or on gguf if local? 
  - Maybe can use code logic to auto run depending on stack.
- Free A100 speed when using private HF space!

### Export
- DSPy code export: Setup and experiment, be able to generate DSPy-Code which represents the setup.

### Section structure
- For the sections: Make them as userfriendly as possible by any means:
  - More fully build out version: Have multiple "levels" of difficulty.
    - 1 is "use simple language, no special terms (besides prompt) at all (no LM/LLM!), explain no concept at all" still provide somewhat useful output
    - 2 offer explainer for some of things you have done, use basic terminology, use bubbles to explain them
    - 3 assume user knows what a dataset, rl, llm, prompt is.
  - Make it steamlined, needs to be simple ui! Maybe add a "enable expert mode" button hidden at the bottom, have the user have a maximally simple experience first. Use global state to copy any inputs on to other modes when switching tabs.
  