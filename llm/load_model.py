from transformers import AutoModelForCausalLM, AutoTokenizer

def load_llm(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cpu",
        torch_dtype="float32"
    )

    model.eval()
    return model, tokenizer
