from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Caminho do modelo base (ex: TinyLlama original)
BASE_MODEL_PATH = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"  # ou o caminho local que usou como base

# Caminho para os pesos LoRA
LORA_PATH = "../model/modelo_treinado_lora_v2"  # caminho até a pasta com o LoRA salvo

# Caminho de saída do modelo final
OUTPUT_DIR = "../model/modelo_mescladp_v2"

# Carregar o modelo base
base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL_PATH)

# Carregar os deltas LoRA
model = PeftModel.from_pretrained(base_model, LORA_PATH)

# Mesclar os pesos do LoRA ao modelo base
model = model.merge_and_unload()

# Salvar o modelo final mesclado
model.save_pretrained(OUTPUT_DIR)

# Salvar o tokenizer
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH)
tokenizer.save_pretrained(OUTPUT_DIR)

print("✅ Modelo mesclado e salvo em", OUTPUT_DIR)
