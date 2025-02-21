tags = ["PROG_LANG", "FRAMEWORK", "ALGORITHM", "LIBRARY"]

training_data = [
    {
        "text": "Para a comparação entre os métodos, foi utilizado a linguagem C para a implementação, junto com a biblioteca Open Multi-Processing [ope 2019] para a paralelização dos algorit-mos e a biblioteca Gnu Scientific Library [gsl 2019] para a estrutura de dados que contém matrizes e vetores, além das funções próprias de cálculo numérico.",
        "entities": [
            [
                62,
                63,
                "PROG_LANG" # C
            ],
            [
                109,
                130,
                "LIBRARY" # Open Multi-Processing
            ],
            [
                194,
                216,
                "LIBRARY" # Gnu Scientific Library
            ]
        ] # OK 0
    },
    {
        "text": "Para isso, foi utilizada a SPar1 [Griebler et al. 2017], que é uma DSL desenvolvida com foco na abstração do desenvolvimento de aplicações de fluxo de dados.",
        "entities": [
            [
                27,
                32,
                "FRAMEWORK" # SPAR1
            ]
        ] # OK 1
    },
    {
        "text": "A SPar se beneficia do mecanismo de anotações padrão do C++ inseridas diretamente no código fonte.",
        "entities": [
            [
                2,
                6,
                "FRAMEWORK" # SPAR
            ],
            [
                56,
                59,
                "PROG_LANG" # C++
            ]
        ] # OK 2
    },
    {
        "text": "Por padrão, a SPar gera código FastFlow e, no passado, foi adicionado na SPar su-porte para geração de código TBB [Hoffmann et al. 2020].",
        "entities": [
            [
                14,
                18,
                "FRAMEWORK" # SPAR[1]
            ],
            [
                73,
                77,
                "FRAMEWORK" # SPAR[2]
            ],
            [
                31,
                39,
                "FRAMEWORK" # FastFlow
            ],
            [
                110,
                113,
                "LIBRARY" # TBB
            ]
        ] # OK 3
    },
    {
        "text": "GrPPI [del Rio Astorga et al. 2016] é uma IPP que envolopa outras soluções como FastFlow, TBB e até mesmo OpenMP.",
        "entities": [
            [
                0,
                5,
                "LIBRARY" # GrPPI
            ],
            [
                80,
                88,
                "FRAMEWORK" # FastFlow
            ],
            [
                90,
                93,
                "LIBRARY" # TBB
            ],
            [
                106,
                112,
                "LIBRARY" # OpenMP
            ]
        ] # OK 4
    },
    {
        "text": "No campo da programação estruturada, FastFlow [Aldinucci et al. 2014] e TBB [Reinders 2007] são bibliotecas C++ que providenciam padrões paralelos prontos para uso (ex: Map, Farm e Pipeline).",
        "entities": [
            [
                37,
                45,
                "FRAMEWORK" # FastFlow
            ],
            [
                72,
                75,
                "LIBRARY" # TBB
            ],
            [
                108,
                111,
                "PROG_LANG" # C++
            ],
            [
                169,
                172,
                "ALGORITHM" # Map
            ],
            [
                174,
                178,
                "ALGORITHM" # Farm
            ],
            [
                181,
                189,
                "ALGORITHM" # Pipeline
            ]
        ] # OK 5
    },
    {
        "text": "Foi observado que a implementação OpenMP ficou no máximo 1,72%% inferior em relação estado-da-arte com Pthreads.",
        "entities": [
            [
                34,
                40,
                "LIBRARY" # OpenMP
            ],
            [
                103,
                111,
                "LIBRARY" # Pthreads
            ]
        ] # OK 6
    },
    {
        "text": "Soma-se a isso, os conceitos sobre o MPI (onde se trabalham conceitos de comunicação e sincronização de processos), bem como o de Programação Paralela (onde se introduz os conceitos de múltiplas execuções em paralelo), principalmente utilizando as linguagens C/C++, contribuı́ram bastante para esses baixos ı́ndices de acertos.",
        "entities": [
            [
                37,
                40,
                "LIBRARY" # MPI
            ],
            [
                259,
                260,
                "PROG_LANG" # C
            ],
            [
                261,
                264,
                "PROG_LANG" # C++
            ]
        ]
    },
    {
        "text": "Primeiro, porque a grande maioria dos alunos, possui um pouco mais de experiência na linguagem Python, e quase nenhuma experiência com as linguagens C/C++.",
        "entities": [
            [
                95 , 101 ,
                "PROG_LANG" # PYTHON
            ],
            [
                149 , 150 ,
                "PROG_LANG" # C
            ],[
                151 , 154 ,
                "PROG_LANG" # C++
            ]
        ]
    },
    {
        "text": "Outro ponto é que o modo SE do GEM5 não suporta as diretivas do OpenMP, que são necessárias para a paralelização dos algoritmos na execução do benchmark.",
        "entities": [
            [
                31 , 
                35 ,
                "FRAMEWORK" # GEM5
            ],
            [
                64 , 
                70 ,
                "LIBRARY"  # OpenMP
            ]
        ]
    },
    {
        "text": "A diferença entre uma e outra é o nı́vel de profundidade no qual ambas ensinam OpenMP, mas a primeira numa profundidade maior.",
        "entities": [
            [
                79 , 
                85 ,
                "LIBRARY" # OpenMP
            ]
        ]
    },
    {
        "text": "Este artigo destaca a aplicação da plataforma OpenCL no ensino prático de arquitetura de computadores considerando o uso de CPU e GPU.",
        "entities": [
            [
                46 , 52 , 
                "LIBRARY" # OpenCL
            ]
        ],
    },
    {
        "text": "Para que os estudantes de Arquitetura de Computadores se familiarizem com a computação paralela, é proposta a utilização de um simulador de sistema completo e a benchmark composto por algoritmos de ordenação parale-lizados com OpenMP.",
        "entities": [
            [
                227 , 233 , 
                "LIBRARY" # OpenMP
            ]
        ],  
    },
    {
        "text": "A Universidade UTN-Bahia Blanca inclui uma nova disciplina denominada parallel processing dentro do curso de Engenharia da Computação. É uma disciplina em que a grande maioria dos alunos estão no seu último ano e basicamente a estrutura da disciplina inclui MPI, Pthreads, OpenMP e OpenCL.",
        "entities": [
            [
                258 , 261 , 
                "LIBRARY" # MPI
            ],
            [
                263 , 271 ,
                "LIBRARY" # Pthreads
            ],
            [
                273 , 279 , 
                "LIBRARY" # OpenMP
            ], 
            [
                282 , 288 ,
                "LIBRARY" # OpenCL
            ]
        ],
    }, 
    {
        "text": "Com o tutorial found in for example, it is possı́vel to construct an API for image recognition using Watson, Node-RED and a fairly simplified coding.",
        "entities": [
            [
                109 , 117 , 
                "FRAMEWORK" # Node-RED
            ]
        ],
    },
    {
        "text": "O nó mais usado para programação é o nó function onde é inserido um código JavaScript, no qual ele pode retornar vários valores em saídas diferentes permitindo o controle de fluxo.",
        "entities": [
            [
                75 , 85 , 
                "PROG_LANG" # JavaScript
            ]
        ],
    },
    {
        "text": "Caso o aluno faça uma simulação utilizando o algoritmo Selection Sort e não tenha modificado o arquivo rcS, será realizada uma ordenação sobre uma lista com 10000 números intei-ros.",
        "entities": [
            [
                55 , 69 ,
                "ALGORITHM" # Selection Sort
            ]
        ],
    },
    {
        "text": "Tabela II CONFIGURAÇÕES PADRÃO DAS ENTRADAS DO benchmark Algoritmo Entrada Algoritmo Entrada Bublle Sort 10000 Shell Sort 1000000 Selection Sort 10000 Merge Sort 1000000 Odd-Even Sort 10000 Quick Sort 1000000.",
        "entities": [
            [93 , 104 , "ALGORITHM"],  # Bublle Sort
            [111 , 121 , "ALGORITHM"], # Shell Sort
            [130 , 144 , "ALGORITHM"], # Selection Sort
            [151 , 161 , "ALGORITHM"], # Merge Sort
            [170 , 183 , "ALGORITHM"], # Odd-Even Sort
            [190 , 200 , "ALGORITHM"], # Quick Sort
        ],
    },
    {
        "text": "Figura 2. Tempo de execução do Bubble Sort, Selection Sort e Odd Even Sort, utilizando um núcleos e quatro núcleos.",
        "entities": [[31 , 42 , "ALGORITHM"], [44 , 58 , "ALGORITHM"], [61 , 74 , "ALGORITHM"]],
    },
    {
        "text": "Figura 3. Tempo de execução do Shell Sort, Merge Sort e Quick Sort, utilizando um núcleos e quatro núcleos.",
        "entities": [[31 , 41 , "ALGORITHM"], [43 , 53 , "ALGORITHM"], [56 , 66 ,"ALGORITHM"]],
    },
    {
        "text": "OpenCL includes a C99 based language for writing kernel code, and the host program can be written in other languages such as: C/C++, Java and Python.",
        "entities": [
            [0, 6, "LIBRARY"], # OpenCL
            [18 , 21 , "PROG_LANG"], # C99
            [126, 127, "PROG_LANG"], # C
            [128 , 131 , "PROG_LANG"], # C++
            [133 , 137 , "PROG_LANG"], # Java
            [142 , 148 , "PROG_LANG"] # Python
        ],
    },
    {
        "text": "O Nó mais usado para programação é o nó function onde é inserido um código JavaScript, no qual ele pode retornar vários valores em saídas diferentes permitindo o controle de fluxo.",
        "entities": [[75 , 85 , "PROG_LANG"]],
    },
    {
        "text": "There are also nodes for programming in Python in versions 2.7 or 3.0.",
        "entities": [[40 , 46 , "PROG_LANG"]],
    },
    {
        "text": "The examples presented, MQTT will be used for exchanging messages between the nodes of Node-RED and the embedded devices (such as Arduino/ESP8266, Raspberry Pi, among others).",
        "entities": [[87 , 95 , "FRAMEWORK"]],
    }
]

if __name__ == '__main__':
    training_data_size = 0

    for element in training_data:
        training_data_size += 1
        text = element['text']
        entities = element['entities']

        print(f'TEXTO: {text}')

        for entity in entities:
            first_index = entity[0]
            last_index = entity[1]
            print(f'ENTIDADE: "{text[first_index:last_index]}" ({first_index}, {last_index}, {entity[2]})')
        
        print()
    
    print(f'Training data size: {training_data_size}')