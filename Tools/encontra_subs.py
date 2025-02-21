import readline
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TestData.test_data import test_data
from TrainingData.training_data import training_data

def encontrar_indices(texto, substring):
    #vamos encontrar todas as ocorrências da substring no texto
    indices = []
    inicio = 0
    while True:
        inicio = texto.find(substring, inicio)
        if inicio == -1:
            break
        fim = inicio + len(substring)
        indices.append((inicio, fim))
        inicio = fim
    return indices

# Pegue os argumentos da linha de comando
if len(sys.argv) != 2:
    print("Usage: python encontra_subs.py <fonte_de_textos>\n")
    print("<fonte_de_textos> é de qual arquivo de texto você deseja usar.")
    print("\tOs arquivos de texto disponíveis são:")
    print("\t0 - test_data")
    print("\t1 - training_data")
    sys.exit(1)

indice_texto = sys.argv[1]

if indice_texto not in ["0", "1"]:
    print("O índice de texto deve ser 0 ou 1.")
    sys.exit(1)

file_to_search = test_data if indice_texto == "0" else training_data

while True:
    response = input("Digite o índice do texto e a string (ou 'sair' para sair): ")
    
    response = response.strip()
    if response == "sair":
        break
    
    partes = response.split()
    if len(partes) != 2:
        print("Entrada inválida. Por favor, digite o índice do texto e a string separados por espaço.")
        print()
        continue

    indice_texto = int(partes[0])
    substring = partes[1]

    # Encontre os índices da substring no texto
    texto = file_to_search[indice_texto][0] if isinstance(file_to_search[indice_texto], list) else file_to_search[indice_texto]['text']
    indices = encontrar_indices(texto, substring)

    print()
    print(f'Texto: {texto}')
    print(f'Substring: "{substring}" em {indices}')
    print()