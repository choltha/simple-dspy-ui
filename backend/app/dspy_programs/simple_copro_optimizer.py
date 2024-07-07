import dspy

class CoproOptimizer:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model

    def optimize_prompt(self, signature, example_task1_input, example_task1_gold_result):
        return f"optimized prompt dummy - signature: {signature}, example_task1_input: {example_task1_input}, example_task1_gold_result: {example_task1_gold_result}"

"""
make signature definable by user (set __docs__?)

### define task
### run copro
### log steps somewhere
### visualize in a primitve way...

"""
