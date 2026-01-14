class CyberCommander:
    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever

    def analyze(self, event):
        context = self.retriever.retrieve(event["raw"])
        
        prompt = f"""
        You are a cyber security commander AI.
        Analyze the following event:

        EVENT: {event}
        CONTEXT: {context}

        Explain threat, intent, and risk.
        """

        response = self.llm.generate(prompt)
        return response