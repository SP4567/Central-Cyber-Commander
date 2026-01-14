from llm.tokenizer import CyberTokenizer
class CyberLLM:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = CyberTokenizer(tokenizer)

    def generate(self, prompt, max_tokens=512):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        output = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.3
        )

        return self.tokenizer.decode(output[0], skip_special_tokens=True)
