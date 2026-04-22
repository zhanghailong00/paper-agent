class WritingPipeline:
    def __init__(self, llm, prompts):
        self.llm = llm
        self.prompts = prompts

    def run_step(self, prompt_template, text):
        prompt = prompt_template.replace("{input}", text)
        return self.llm.call(prompt)

    def run(self, text):
        # Step 1: translate
        step1 = self.run_step(self.prompts["translate"], text)

        # Step 2: rewrite
        step2 = self.run_step(self.prompts["rewrite"], step1)

        # Step 3: de-ai
        step3 = self.run_step(self.prompts["deai"], step2)

        # Step 4: review
        step4 = self.run_step(self.prompts["review"], step3)

        return {
            "translate": step1,
            "rewrite": step2,
            "deai": step3,
            "review": step4
        }