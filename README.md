# Trabalho 2 de PLN

## Descrição
Este projeto é parte da disciplina de Processamento de Linguagem Natural (PLN) e tem como objetivo desenvolver um modelo NER com base no pt_core_news_sm que identifica entidades relacionadas à computação, como linguagens de programação, frameworks, bibliotecas e algoritmos. O modelo foi treinado com artigos da SBC (Sociedade Brasileira de Computação).

## Conjunto de Dados
Este projeto é uma prova de conceito, portanto o conjunto de dados usado foi muito pequeno. Ele se encontra no arquivo `training_data.py` como um array de tuplas contendo as tags que criamos. Os textos no array foram extraídos de artigos públicos da SBC que estão disponíveis [aqui](https://drive.google.com/drive/folders/1ZltMA-gIdFodY4-lNXMJUITI7YP8JKGe?usp=sharing).

## Instruções de Execução
1. Clone o repositório:
    ```bash
    git clone https://github.com/henrique/trabalho-2-pln.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd trabalho-2-pln
    ```
3. Instale as dependências:
    ```bash
    pip install -U pip setuptools wheel
    pip install -U spacy
    python -m spacy download pt_core_news_sm
    ```
4. Treine o modelo:
    ```bash
    python Trainer.py
    ```
5. Teste o modelo:
    ```bash
    python Tester.py
    ```

## Licença
Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).

