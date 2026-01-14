# llm/tokenizer.py

import re

IP_REGEX = r"(?:\d{1,3}\.){3}\d{1,3}"
HASH_REGEX = r"\b[a-fA-F0-9]{32,64}\b"
CVE_REGEX = r"CVE-\d{4}-\d{4,7}"

class CyberTokenizer:
    def __init__(self, base_tokenizer):
        self.base_tokenizer = base_tokenizer

    def preprocess(self, text: str) -> str:
        text = re.sub(IP_REGEX, r"[IP]\g<0>[/IP]", text)
        text = re.sub(HASH_REGEX, r"[HASH]\g<0>[/HASH]", text)
        text = re.sub(CVE_REGEX, r"[CVE]\g<0>[/CVE]", text)
        return text

    def __call__(self, text, **kwargs):
        processed = self.preprocess(text)
        return self.base_tokenizer(processed, **kwargs)

    def decode(self, tokens, **kwargs):
        return self.base_tokenizer.decode(tokens, **kwargs)