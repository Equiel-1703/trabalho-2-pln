import spacy
from spacy.training import Example
from TrainingData.training_data import training_data, tags
import random
import sys

OUTPUT = "NER_CComp"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python Trainer.py <número de épocas>")
        sys.exit(1)

    epochs = int(sys.argv[1])
    print(f"Treinando o modelo por {epochs} épocas...")
    print()

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

    nlp.to_disk(OUTPUT)

    print(f"Modelo treinado e salvo em {OUTPUT}/")
    print()