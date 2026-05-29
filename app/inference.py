from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer

MODEL_PATH = "models/onnx_production"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

model = ORTModelForSeq2SeqLM.from_pretrained(
    MODEL_PATH
)

def summarize(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_length=150,
        min_length=30,
        num_beams=4
    )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary