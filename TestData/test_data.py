test_data = [
    (
        "O PyTorch é um framework popular.",
        {
            "entities": [
                (2, 9, "FRAMEWORK")
            ]
        }
    ),
    (
        "O algoritmo A* é usado em IA.",
        {
            "entities": [
                (12, 14, "ALGORITHM")
            ]
        }
    ),
    (
        "O PyTorch e TensorFlow são frameworks poderosos para deep learning em Python.",
        {
            "entities": [
                (2, 9, "FRAMEWORK"),
                (12, 22, "FRAMEWORK")
            ]
        }
    ),
    (
        "O algoritmo A* é usado em rotas de entrega.",
        {
            "entities": [
                (12, 14, "ALGORITHM")
            ]
        }
    ), # OK 3
    (
        "A biblioteca Pandas facilita a manipulação de dados.",
        {
            "entities": [
                (13, 19, "LIBRARY")
            ]
        }
    ), # OK 4
    (
        "Java e Python são linguagens populares.",
        {
            "entities": [
                (0, 4, "PROG_LANG"),
                (7, 13, "PROG_LANG")
            ]
        }
    ), # OK 5
    (
        "C99-based code is not supported by the compiler.",
        {
            "entities": [
                (0, 3, "PROG_LANG")
            ]
        }
    ), # OK 6
]
