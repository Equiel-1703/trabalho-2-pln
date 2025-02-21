import sys
from dados_treinamento import dados_treinamento

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
if len(sys.argv) != 3:
    print("Usage: python encontra_subs.py <indice_do_texto> <substring>")
    sys.exit(1)

indice_texto = sys.argv[1]
substring = sys.argv[2]

# Encontre os índices da substring no texto
texto = dados_treinamento[int(indice_texto)]['text']
indices = encontrar_indices(texto, substring)

print(f'Texto: {texto}')
print(f'Substring: "{substring}" em {indices}')