from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_DIR = "../model/modelo_mescladp_v2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_DIR,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Inicializa histórico com instruções de sistema
history = [
    ("system",
     "Você é um assistente médico que realiza triagem de sintomas e oferece diagnósticos e orientações.")
]

def build_prompt(history):
    parts = []
    for role, text in history:
        if role == "system":
            parts.append(f"<|system|>\n{text}\n")
        elif role == "user":
            parts.append(f"<|user|>\n{text}\n")
        elif role == "assistant":
            parts.append(f"<|assistant|>\n{text}\n")
    parts.append("<|assistant|>\n")
    return "".join(parts)

while True:
    user_input = input("Você: ")
    if user_input.lower() in ("sair", "exit", "quit"):
        break

    history.append(("user", user_input))
    prompt = build_prompt(history)

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        no_repeat_ngram_size=2,
        eos_token_id=tokenizer.eos_token_id
    )
    resposta = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    ).strip()

    history.append(("assistant", resposta))
    print(f"Assistente: {resposta}\n")
