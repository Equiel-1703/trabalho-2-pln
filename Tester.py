from Trainer import OUTPUT
from TestData.test_data import test_data

import spacy
from spacy.scorer import Scorer
from spacy.training import Example

import sys
import regex as re

def pre_process_text(text):
    # Remove caracteres especiais e hífens do texto, mantendo apenas letras, números e espaços.
    def clean_text(text):
        text = re.sub(r'[^a-zA-Z0-9\s\-\*]', ' ', text)  # Remove tudo que não for letra, número, espaço, hífen e asterisco
        text = re.sub(r'-+', ' ', text)  # Remove hífens
        text = re.sub(r'\s+', ' ', text).strip()  # Remove espaços extras
        return text
    
    text = clean_text(text)
    return text

def evaluate(examples, nlp):
    scorer = Scorer()
    examples_objs = []

    for (text, entities) in examples:
        doc = nlp(text)
        print(doc.ents)
        example = Example.from_dict(doc, entities)
        examples_objs.append(example)
    
    scores = scorer.score(examples_objs)
    return scores

# Função para formatar a saída
def format_score(score):
    formatted = ""
    for metric, value in score.items():
        if isinstance(value, (int, float)):  # Verifica se é um número
            formatted += f"{metric}: {value:.4f}\n"
        elif isinstance(value, dict):  # Se for um dicionário, imprimimos de forma legível
            formatted += f"{metric}: \n"
            for sub_metric, sub_value in value.items():
                formatted += f"  {sub_metric}: {sub_value:.4f}\n" if isinstance(sub_value, (int, float)) else f"  {sub_metric}: {sub_value}\n"
        else:
            formatted += f"{metric}: {value}\n"  # Para outros tipos de dados
    return formatted

# Carregar o modelo treinado
print(f"Carregando o modelo {OUTPUT}...")
nlp = spacy.load(OUTPUT)

if nlp is None:
    print("Erro ao carregar o modelo.")
    sys.exit(1)

if "ner" not in nlp.pipe_names:
    print("O modelo não possui um componente NER.")
    sys.exit(1)

# Testar o modelo treinado
print(f"Modelo {OUTPUT} carregado.")
print()
print("Carregando e pré-processando os textos de teste...")

dados_processados = []
for (texto, entidades) in test_data:
    texto_processado = pre_process_text(texto)
    dados_processados.append((texto_processado, entidades))

print("Textos pré-processados:")

for (texto, _) in dados_processados:
    print(texto)

print()
print("Testando o modelo...")

results = evaluate(dados_processados, nlp)
# print(format_score(results))
print(results)
print()