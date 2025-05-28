import json

# Exemplo simplificado com algumas doenças da CID-10
doencas_cid10 = [
    {
        "codigo": "J45",
        "nome": "Asma",
        "descricao": "Asma é uma doença inflamatória crônica das vias aéreas que causa dificuldade para respirar.",
        "tratamento": "O tratamento inclui uso de broncodilatadores e corticosteroides inalatórios.",
        "sintomas": "Sintomas comuns são falta de ar, chiado no peito e tosse."
    },
    {
        "codigo": "E11",
        "nome": "Diabetes Mellitus tipo 2",
        "descricao": "Diabetes tipo 2 é uma doença crônica caracterizada pela resistência à insulina.",
        "tratamento": "O tratamento envolve dieta, exercícios físicos e medicações hipoglicemiantes.",
        "sintomas": "Sintomas incluem sede excessiva, aumento da fome e urina frequente."
    },
    {
        "codigo": "I10",
        "nome": "Hipertensão Essencial",
        "descricao": "Hipertensão é o aumento persistente da pressão arterial.",
        "tratamento": "Inclui mudança de estilo de vida e uso de anti-hipertensivos.",
        "sintomas": "Geralmente assintomática, mas pode causar dores de cabeça e tontura."
    }
]

# Instruções para cada doença - exemplos variados
tipos_instrucao = [
    "Explique o que é {nome}.",
    "Como tratar {nome}?",
    "Quais são os sintomas de {nome}?",
    "O que é {nome}?",
    "Me fale sobre {nome}.",
]

dados_gerados = []

for doenca in doencas_cid10:
    for instrucao in tipos_instrucao:
        texto_instrucao = instrucao.format(nome=doenca["nome"])
        if "sintomas" in instrucao.lower():
            resposta = doenca["sintomas"]
        elif "tratar" in instrucao.lower():
            resposta = doenca["tratamento"]
        else:
            resposta = doenca["descricao"]
        
        dados_gerados.append({
            "instruction": texto_instrucao,
            "input": "",
            "output": resposta
        })

# Salvar no arquivo JSON
with open("dados_curados.json", "w", encoding="utf-8") as f:
    json.dump(dados_gerados, f, ensure_ascii=False, indent=2)

print(f"{len(dados_gerados)} exemplos gerados e salvos em dados_curados.json")
