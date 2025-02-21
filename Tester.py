from Trainer import OUTPUT
from TestData.test_data import test_data

import spacy
from spacy.scorer import Scorer
from spacy.training import Example

import sys
import regex as re

# Pre-process the text before passing it to the model
def pre_process_text(text):
    # This will remove special characters, hyphens and extra spaces
    def clean_text(text):
        text = re.sub(r'[^a-zA-Z0-9\s\-\*]', ' ', text)  # Removes everything except letters, numbers, spaces, hyphens and asterisks
        text = re.sub(r'-+', ' ', text)  # Removes hyphens
        text = re.sub(r'\s+', ' ', text).strip()  # Cleans up extra spaces
        return text
    
    text = clean_text(text)
    return text

# Evaluation data is in tuples, we must convert it to a list of Doc objects
def create_docs(nlp, evaluation_data):
    docs = []
    for (text, annotations) in evaluation_data:
        doc = nlp.make_doc(text) # Create a Doc object from the text
        doc.ents = [doc.char_span(start, end, label, alignment_mode="strict")
                    for start, end, label in annotations.get('entities', [])
                    if doc.char_span(start, end, label, alignment_mode="strict") is not None] # Set entities
        docs.append(doc)
    return docs

# Evaluate the model
def evaluate_model(nlp, evaluation_docs):
    scorer = Scorer()
    examples = [] # Create an empty list to store Example objects
    for gold_doc in evaluation_docs:
        predicted_doc = nlp(gold_doc.text)
        # Create an Example object from predicted and gold docs
        example = Example(predicted_doc, gold_doc) # Order is (predicted, reference)
        examples.append(example) # Add the Example to the list

    scores = scorer.score(examples) # Now pass the list of Example objects to scorer.score()
    return scores

# Evaluate the model and print the predicted entities
def evaluate_model_verbose(nlp, evaluation_docs):
    scorer = Scorer()
    examples = []
    example_count = 0 # Counter for printed examples

    print("\n------------ Resultados ------------")

    for gold_doc in evaluation_docs:
        predicted_doc = nlp(gold_doc.text)
        example = Example(predicted_doc, gold_doc)
        examples.append(example)

        print(f">> Teste {example_count + 1}:")
        print(f"Texto: {gold_doc.text}")
        print("Entidades de Referência (Gold):")
        for ent in gold_doc.ents:
            print(f"  {ent.text} ({ent.label_})")
        print("Entidades Encontradas:")
        for ent in predicted_doc.ents:
            print(f"  {ent.text} ({ent.label_})")
        example_count += 1
        print()
        
    scores = scorer.score(examples)
    return scores

# Format the evaluation metrics for better readability
def format_score(score):
    formatted = ""

    formatted += f"* Precision: {score['ents_p']:.4f}\n"
    formatted += f"* Recall: {score['ents_r']:.4f}\n"
    formatted += f"* F1-score: {score['ents_f']:.4f}\n"
    formatted += f"* Accuracy: \n"

    for ent_type, accuracy in score['ents_per_type'].items():
        formatted += f"\t{ent_type}: {accuracy['p']:.4f}, {accuracy['r']:.4f}, {accuracy['f']:.4f}\n"

    return formatted

VERBOSE = False

print(f"Spacy versão: {spacy.__version__}")

if len(sys.argv) > 1:
    if sys.argv[1] == "-v" or sys.argv[1] == "--verbose":
        VERBOSE = True

# Carregar o modelo treinado
print(f"Carregando o modelo {OUTPUT}...")
nlp = spacy.load(OUTPUT)

if nlp is None:
    print("Erro ao carregar o modelo.")
    sys.exit(1)

if "ner" not in nlp.pipe_names:
    print("O modelo não possui um componente NER.")
    sys.exit(1)

print(f"Modelo {OUTPUT} carregado.")
print()
print("Carregando e pré-processando os textos de teste...")

dados_processados = []
for (texto, entidades) in test_data:
    texto_processado = pre_process_text(texto)
    dados_processados.append((texto_processado, entidades))

print("\n------ Textos Pré-processados ------")
for (i, dados) in enumerate(dados_processados):
    print(f"Texto {i + 1}: {dados[0]}")
print()

print("Criando objetos Doc para os textos de teste...")
gold_docs = create_docs(nlp, dados_processados)

print()
print("Testando o modelo...")

if VERBOSE:
    eval = evaluate_model_verbose
else:
    eval = evaluate_model

metricas_avaliacao = eval(nlp, gold_docs)

print("\n------ Métricas de Desempenho ------")
print(format_score(metricas_avaliacao))
print()