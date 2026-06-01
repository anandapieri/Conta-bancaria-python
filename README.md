# Sistema de Conta Bancária em Python

Projeto desenvolvido em Python com o objetivo de praticar Programação Orientada a Objetos (POO), encapsulamento, manipulação de listas e construção de aplicações interativas via terminal.

## Funcionalidades

* Realizar depósitos
* Realizar saques
* Consultar saldo
* Consultar histórico de transações
* Validação de operações inválidas
* Controle de saldo disponível

## Tecnologias utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* Git
* GitHub

## Estrutura do projeto

```text
📁 conta-bancaria-python
│
├── conta_bancaria.py
├── main.py
└── README.md
```

## Conceitos praticados

Este projeto foi desenvolvido para praticar:

* Classes e Objetos
* Métodos
* Encapsulamento
* Atributos privados
* Listas
* Estruturas condicionais
* Estruturas de repetição
* Tratamento de regras de negócio
* Organização de código em múltiplos arquivos

## Como executar o projeto

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd conta-bancaria-python
```

Execute o programa:

```bash
python main.py
```

## Exemplo de utilização

```text
Escolha uma opção:

1. Depositar valor
2. Sacar valor
3. Exibir saldo
4. Exibir histórico de transações
5. Sair
```

## Regras implementadas

### Depósito

* O valor informado deve ser maior que zero.
* Depósitos válidos são registrados no histórico.

### Saque

* O valor informado deve ser maior que zero.
* Não é permitido sacar valores superiores ao saldo disponível.
* Tentativas de saque sem saldo suficiente são registradas no histórico.

### Extrato

O sistema mantém um histórico de todas as transações realizadas durante a execução do programa.

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos fundamentais de Programação Orientada a Objetos, como encapsulamento de atributos, separação de responsabilidades entre classes e construção de sistemas orientados a objetos utilizando Python.

## Autora

Desenvolvido por Ananda Pieri.