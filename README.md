Fine-Tuning de LLM com TinyLlama 1.1B e LoRA
Este projeto faz o fine-tuning de uma Large Language Model (LLM) usando o modelo TinyLlama 1.1B. A técnica de LoRA é usada para ajustar o modelo de forma eficiente (meu notebook não tem GPU :c), mesclando os deltas do modelo e reduzindo o custo computacional.

Descrição
O objetivo deste projeto é adaptar o modelo TinyLlama 1.1B para novas tarefas usando LoRA. Essa abordagem permite realizar ajustes rápidos e eficientes no modelo, aproveitando os recursos de forma otimizada.

Requisitos
Antes de rodar o projeto, você vai precisar da:

Criar o ambiente no Anaconda
Instalar as dependências:

conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install transformers
pip install peft
pip install trf

ao instalar o transformers e trf diversas outras dependências serão instaladas automaticamente para ambas funcionem corretamente

vá até o diretório e execute python fine_tuning.py
