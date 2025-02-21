from TestData.test_data import test_data

def analyze_entity_distribution(evaluation_data):
    entity_counts = {}
    for text, annotations in evaluation_data:
        for start, end, label in annotations.get('entities', []):
            entity_counts[label] = entity_counts.get(label, 0) + 1
    return entity_counts

entity_distribution = analyze_entity_distribution(test_data)
print("Distribuição de entidades nos dados de teste:")
print(entity_distribution)