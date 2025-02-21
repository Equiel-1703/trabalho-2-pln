test_data = [
    (
        "O OpenMP é uma biblioteca popular.",
        {
            "entities": [
                (2, 8, "LIBRARY")
            ]
        }
    ),
    (
        "O algoritmo Bubble Sort é um dos mais simples.",
        {
            "entities": [
                (12, 23, "ALGORITHM")
            ]
        }
    ),
    (
        "Pthreads e OpenMP são bibliotecas de programação paralela.",
        {
            "entities": [
                (0, 8, "LIBRARY"),
                (11, 17, "LIBRARY")
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
        "A biblioteca OpenCL é usada para programação de GPUs.",
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
