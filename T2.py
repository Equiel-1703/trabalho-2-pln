import spacy
from spacy.tokens import Span
from spacy.training import Example
import random

# Carregar modelo base do spaCy
nlp = spacy.load("pt_core_news_sm")

# Adicionar novas entidades ao modelo
labels = ["PROG_LANG", "FRAMEWORK", "ALGORITHM", "LIBRARY"]

# Criar um componente NER personalizado
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Adicionar os novos rótulos ao NER
for label in labels:
    ner.add_label(label)

# Dados de treinamento (exemplo)
train_data = [
    ("O TensorFlow é um framework amplamente usado em Machine Learning.",
     {"entities": [(2, 12, "FRAMEWORK")]}),
    ("O algoritmo Dijkstra é muito utilizado em grafos.",
     {"entities": [(12, 20, "ALGORITHM")]}),
    ("A biblioteca NumPy facilita operações com matrizes.",
     {"entities": [(13, 18, "LIBRARY")]}),
    ("Python e Java são linguagens populares.",
     {"entities": [(0, 6, "PROG_LANG"), (9, 13, "PROG_LANG")]}),
]

# Criar exemplos para treino
examples = []
for text, annotations in train_data:
    doc = nlp.make_doc(text)
    examples.append(Example.from_dict(doc, annotations))

# Treinar o modelo
epochs = 100
optimizer = nlp.resume_training()
for _ in range(epochs):  # Número de épocas
    random.shuffle(examples)
    losses = {}
    nlp.update(examples, drop=0.5, losses=losses)

# Testar o modelo treinado
text1 = "O PyTorch e TensorFlow são frameworks poderosos para deep learning em Python."
text2 = "O algoritmo A* é usado em rotas de entrega."
text3 = "A biblioteca Pandas facilita a manipulação de dados."
text4 = "Java e Python são linguagens populares."

print()
for text in [text1, text2, text3, text4]:
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Texto: {text}\nEntidades reconhecidas: {entities}\n")

print(f"Épocas: {epochs}")
