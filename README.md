# Simple DSPy Ui

## Goals of project
Enable everyone to profit from DSPy super prompts.

Main focus should be ease of use, easy slope on learning curve.

## Usecases:
- switch existing pipeline to new model, but not time to adapt all prompts
  - just provide meta of what you are doing
  - metric optional (else f1 on example data)
  - provide examples (1000) from real world usage
    - random shuffle input (fixed seed! for reproducability)
    - split train/dev/test
    - run mipro
- new program, want to find good prompt as I have some false positives and the prompts are getting too long.
- new program and I don't want to craft the prompts on my own, but have data what i have before and what after, so just do it for me.
- downgrading to less expensive model but maintaining performance. (or test if this works)
- changing to different model, to see if it can do better (metric needs to be defined here to avoid having) 
- potential for auto-self-improve-flywheel

## UX Goals
Maximum transparency:
- Simple wording for first examples, then progress to advanced explainations / DSPy wording as we progress
- Show progress (resulting prompts) (diff view betweeen steps?), evals, etc? (see steamlit dashboards, but with gradio?)

Explainer, that DSPy is basically machinelearning applied to prompts and needs examples for train/test.
Add tooling to generate exactly such initial data to get the DSPy flywheel going.

## Sections / Tabs

### Tab 1: Easy, guardrailed intro to the power of DSPy
- show one mindblowing example with MIPROv2 on first Tab. As hook, present and Link to bold claims where mipro kills it (vs human prompter for example)
- "use simple language, no special terms (besides prompt) at all (no LM/LLM!), explain no concept at all" still provide somewhat useful output
- Go full static examples on first tab, no manual editing allowed (we want to use cache for everything!). All example text hardcoded (might have 2 scenarios to chose from tho)
  - As we are using cache we know EXACTLY what results to expect and can explain them in detail. Also we can cherry-pick a run with generations which are good for learning and for-human-learner-demonstration purposes.
- UX:  just buttons, so everyone can wrap his mind around it without seeing any code abstraction for first step.
  - Notebooks are similar but more technical, a lot of people already stop there because they don't know how to use them and they can be pretty intimidating on their own. Everyone loves a simple button UI tho.
- Guide the user through the DSPy-Preparation and optimisation progress step by step.
  - what do we want to do?
  - define basics
  - hide metric for now. Explain metric later. "Now how does it know this is a good result and which not?"
  - provide 1-5 example explicitly, rest in the list (engouh so user reads one and gets what the examples are about but is not intimidated/bored by reading 10 examples
  - eval before optimisation
    - run the "barebone" dspy query
    - run one "half baked" human query for comparison/ baseline for later
  - run MIPROv2
    - log and show the MIPROv2 queries (or copy+adapt MIPROv2 with minor changes to do so)
      - expecially the meta queries "what is this about?" etc.
    - explain certain examples in markdown blocks
      - provide rest of list / runs in tabular display
  - show end result prompt and difference in evals.
=> example is maximally guardrailed, making usage super easy.

### Tab 2: Even more power, more responsibility. Get more technical, DSPy terminology, and more
- Main goal: Get into concise DSPy wording (this could also be just Tooltips/foldables in Tab1 for now...), maybe show some code snippets?
  - use DSPy wording for everything (explain in reference to tab 1 for transition ("we called this a good example which shows how to do it/ideal answer ... this is now just cold a "gold answer" from here on))
- same layout in essentials as Tab1 to keep it simple !!
- Eventually explain metric here (and have a 2nd metric, also cached) as alternative (llm as a judge for example (which could be a sub dspy program, but not explained, thats too much for now))
- Export Button for Explainer code (or Link to github where the full example code is (but maybe optimized for local usage in one big file, not the gradio structuire?, Or we could use one big "examplev2.py" in the root and put everything there, load that one from gradio. Not really nice for project but its educational so that beats overengineered app structure for me.)

### Tab 3: Bring your own usecase & data.
- Has sub Tabs (to hide complexity at start
- "Overview"
  - List different usecases, have explainers and recommendations for each one
    - Usecases see above
  - recommend Miprov2 as allrounder base recommendation for best results 
  - recommend copro for super lazy (VALIDATE if mipro is better or how fast it overfits if we provide just 5 train examples)
- Main DSPy MIPRO Tab 1:
  - API Key input, OR choice to go with phi3-medium on HF Zero space
  - how many eval examples do we need min? 10, 20, 50?)
    - User Defined metric as alternative
- Synthetic Data generation TAb
  - If you want to start a project but don't have any data, this is for you.
  - this is non DSPy stuff but needed to bootstrap usecases by users. See Argilla for inspiration.
- Export Button for Code based on what user defined in interface.

## How to run
- Install pdm if not installed yet
- `cd backend`
- `pdm install`
- `pdm run main.py`

## Techstack
- dspy
- gradio for max prototyping speed and educational ui, use on HF with Zero GPUs
  - need to validate if I can even use HF zero with DSPy.

### Hardware
- Base: Standard HF space (DSPy on its own doesn't need much juice)
- Use Cached for first 2 Tabs, so no external connections should be necessary. (Maybe use 2 Models, like GPT-4o and Phi3-medium-4k)
- For own data Tab: User can choose:
  - Run on HF Zero with phi3-medium-4k
  - Provide API key and openAI-compatible endpoint (with default for just openai (maybe hint at using openrouter for basically ALL LMs available ...))
  - When run locally, llama.cpp / ollama can be used to run Phi3-med-4k on device (also phi3-mini as alternative for almost any device ...)

## Privacy
- Users should know stuff gets cached (forever?), user management probably not tirival to implement.
- Be up front about it.
- Offer "Copy Space" button for people who want privacy.

## Credits
- DSPy is the backbone of this project
- Hugginface for free Zero GPUs

## Examples
- Currently I use short stories, but i think logic puzzles are way more fun!
- Classical get X items across the river. But with other items. Like dog, cat, fish. Fix, chicken, stack of grain. Lion, zebra haybale. monkey, bannana coconut. 
- Jokes? Could that work (for a narrow type of jokes)
  - Topic -> joke; tomatoes; Three tomatoes cross a street. One gets driven over. The other ones say: come on, ketch up!
- summarisation into tasks! This might be something every 2nd user tries to build, so this might resonate well.

## Ideas

### DSPy Optimisation
- Use partial examples to get sub points of examples going with fewer tokens.
