import spacy
from spacy.training import Example
from TrainingData.training_data import training_data, tags
import random
import sys

if len(sys.argv) != 2:
    print("Use: python T2.py <número de épocas>")
    sys.exit(1)

epochs = int(sys.argv[1])

# Carregar modelo base do spaCy
nlp = spacy.load("pt_core_news_sm")

# Criar um componente NER personalizado
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Adicionar os novos rótulos ao NER
for tag in tags:
    ner.add_label(tag)

# Criar exemplos para treino
examples = []
for element in training_data:
    text = element["text"]

    doc = nlp.make_doc(text)
    examples.append(Example.from_dict(doc, {"entities": element["entities"]}))

# Treinar o modelo
optimizer = nlp.resume_training()
for _ in range(epochs):  # Número de épocas
    random.shuffle(examples)
    losses = {}
    nlp.update(examples, drop=0.5, losses=losses)

# Testar o modelo treinado
print("Testando o modelo treinado...\n")

text1 = "O PyTorch e TensorFlow são frameworks poderosos para deep learning em Python."
text2 = "O algoritmo A* é usado em rotas de entrega."
text3 = "A biblioteca Pandas facilita a manipulação de dados."
text4 = "Java e Python são linguagens populares."
text5 = "C99-based code is not supported by the compiler."

print()
for text in [text1, text2, text3, text4, text5]:
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Texto: {text}\nEntidades reconhecidas: {entities}\n")

print(f"Épocas: {epochs}")
