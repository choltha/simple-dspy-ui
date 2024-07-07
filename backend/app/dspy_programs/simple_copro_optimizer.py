import dspy

class CoproOptimizer:
    def __init__(self, target_model, optimizer_model):
        self.target_model = target_model
        self.optimizer_model = optimizer_model

    def optimize_prompt(self, signature_text, example_task1_input_text, example_task1_gold_result_text):
        dspy.settings.configure(lm=self.target_model)
        class CoTSignature(dspy.Signature):
            """Will-be-replaced-dynamically later"""
            question = dspy.InputField(desc="Context") #todo fixme!
            answer = dspy.OutputField(desc="Output") #todo fixme!

        class CoTPipeline(dspy.Module):
            def __init__(self):
                super().__init__()

                self.signature = CoTSignature
                self.signature.__doc__=signature_text # dynamically override!
                self.predictor = dspy.ChainOfThought(self.signature)

            def forward(self, question):
                result = self.predictor(question=question)
                return dspy.Prediction(
                    answer=result.answer,
                    reasoning=result.rationale,
                )

        from dspy.evaluate import Evaluate

        def metric(example, pred, trace=None):
            answer_EM = dspy.evaluate.answer_exact_match(example, pred)
            return answer_EM
        example1 = dspy.Example({"question": example_task1_input_text, "answer": example_task1_gold_result_text}).with_inputs("question")
        devset = [example1]
        evaluate = Evaluate(devset=devset, metric=metric, num_threads=1, display_progress=True, display_table=False)

        from dspy.teleprompt import COPRO

        teleprompter = COPRO(
            metric=metric,
            verbose=True,
        )

        kwargs = dict(num_threads=1, display_progress=True, display_table=0) # Used in Evaluate class in the optimization process

        compiled_prompt_opt = teleprompter.compile(CoTPipeline, trainset=devset, eval_kwargs=kwargs)
    
        import debugpy
        debugpy.listen(("localhost", 5678))
        debugpy.wait_for_client()
        debugpy.breakpoint()

        return compiled_prompt_opt
"""
make signature definable by user (set __docs__?)

### define task
### run copro
### log steps somewhere
### visualize in a primitve way...

"""
