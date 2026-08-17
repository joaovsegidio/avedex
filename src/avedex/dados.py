import json
from pathlib import Path

CAMINHO_PROJETO = Path(__file__).resolve().parents[2]

CAMINHO_DATASET = CAMINHO_PROJETO / "data" / "avedex_dataset_midias.json"

def carregar_dataset(caminho=CAMINHO_DATASET):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dataset = json.load(arquivo)
    return dataset

def carregar_aves():
    dataset = carregar_dataset()

    return dataset.get("aves", [])

def obter_fontes_globais():
    dataset = carregar_dataset()
    
    return dataset.get("fontes_globais", {})