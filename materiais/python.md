
# Introdução ao Python

Bem-vindo(a) ao material de introdução ao Python! Python é uma linguagem de programação popular, conhecida por sua simplicidade e legibilidade. Aqui, você encontrará os seguintes tópicos:

1. O que é Python?
2. Instalação do Python
3. Hello World em Python
4. Variáveis em Python
5. Principais Tipos de Dados em Python
6. Estruturas Condicionais e Operadores Lógicos em Python
7. Estruturas de Repetição em Python
8. Tratamento de Exceções em Python
9. Orientação a Objetos em Python

## O que é Python? 

Python (nome inspirado no grupo de comédia britânico [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)) é uma linguagem de programação de alto nível, interpretada e de propósito geral. Foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Desde então, Python tem crescido em popularidade e é amplamente utilizado em diversas áreas, como Desenvolvimento Web, Ciência de Dados, Inteligência Artificial, RPA (Robotic Process Automation), entre outros.

Ainda, a linguagem de programação Python possui as seguintes características:

- **Simplicidade**: Python possui uma sintaxe limpa e fácil de aprender, o que o torna uma excelente escolha para iniciantes.
- **Legibilidade**: O código Python é altamente legível e semelhante à linguagem natural, facilitando a compreensão mesmo para quem está começando.
- **Versatilidade**: Python é uma linguagem versátil, adequada para uma ampla gama de aplicações, desde scripts simples até projetos complexos.


## Instalação do Python

Para começar a programar em Python, você precisará instalá-lo em seu sistema. Existem várias maneiras de fazer isso, mas a forma mais comum é baixar e instalar o Python a partir do site oficial [python.org](https://www.python.org/downloads/).


### Windows

1. Acesse [python.org](https://www.python.org/) e clique no link de download.
2. Execute o instalador baixado e siga as instruções de instalação.
3. Verifique se a opção "Adicionar Python ao PATH" está marcada durante a instalação.

### Linux

Muitas distribuições Linux já vêm com Python pré-instalado. No entanto, você pode instalar o Python utilizando o gerenciador de pacotes da sua distribuição.

Por exemplo, no Ubuntu, você pode instalar o Python 3 executando o seguinte comando no terminal:

```bash
sudo apt-get install python3
```

## Hello World em Python

Agora que o Python está instalado, vamos escrever nosso primeiro algoritmo. Abra um editor de texto (sugestão [VSCode](https://code.visualstudio.com/download)) e digite o seguinte código:

```python
print("Hello World!")
```

Salve o arquivo com a extensão .py (por exemplo, run.py). Em seguida, abra o terminal, navegue até o diretório onde o arquivo foi salvo e execute o programa digitando:

```bash
python3 run.py
```

## Variáveis em Python

Neste tutorial, você aprenderá sobre variáveis em Python. Variáveis são contêineres para armazenar dados. Python é uma linguagem de programação dinamicamente tipada, o que significa que você não precisa declarar explicitamente o tipo de uma variável antes de usá-la.

### Declarando Variáveis

Na Linguagem de Programação Python, você pode declarar uma variável atribuindo um valor a ela. Abaixo alguns exemplos de declaração de variáveis.

```python
# Exemplos de declaração de variáveis
nome = "Victor"        # String
idade = 29             # Inteiro
altura = 1.71          # Ponto flutuante
é_estudante = False    # Booleano
```

### Nomes de Variáveis
Ao escolher nomes para suas variáveis, lembre-se de seguir estas regras:

1. O nome da variável deve começar com uma letra (a - z, A - Z) ou um sublinhado (_).
2. O nome da variável não pode começar com um número, mas pode conter números depois.
3. O nome da variável só pode conter caracteres alfanuméricos e sublinhados (A-z, 0-9 e _).
4. Os nomes das variáveis são sensíveis a maiúsculas e minúsculas (por exemplo, nome e Nome são variáveis diferentes).

### Convenções de Nomenclatura

Ao nomear suas variáveis, é recomendável seguir as seguintes convenções:

1. Use nomes descritivos que indiquem o propósito da variável.
2. Use letras minúsculas para nomes de variáveis.
3. Se o nome da variável for composto por várias palavras, separe-as usando sublinhados (snake_case).
4. Evite usar palavras reservadas do Python e nomes de funções embutidas como nomes de variáveis.

Ainda, para convenções gerais da linguagem de programação Python você pode consultar o [PEP 8 - Style Guide](https://peps.python.org/pep-0008/).


## Principais Tipos de Dados em Python

Python suporta uma variedade de tipos de dados para lidar com diferentes tipos de informações. Aqui estão os principais:

### Números (int, float, complex)

- **int**: Representa números inteiros, como 5, -3, 1000, etc.
- **float**: Representa números decimais, como 3.14, -0.001, 2.0, etc.
- **complex**: Representa números complexos na forma `a + bj`, onde `a` e `b` são números reais e `j` é a unidade imaginária.

### Strings

- **str**: Sequência de caracteres, que podem ser definidas usando aspas simples (' '), aspas duplas (" ") ou aspas triplas (''' ''' ou """ """). Por exemplo, no código abaixo há uma representação de uma string em Python.
```python
variavel_string = 'Olá'
```

### Booleanos

- **bool**: Tipo de dado booleano, que pode ter apenas dois valores: True (verdadeiro) e False (falso). É usado para representar condições lógicas. Por exemplo, no código abaixo há uma representação de uma variável booleana em Python.
```python
variavel_booleana = True
```


### Listas

- **list**: Coleção ordenada e mutável de itens. Os itens podem ser de tipos diferentes e você pode modificar, adicionar ou remover itens conforme necessário. Por exemplo, no código abaixo há uma representação de uma lista em Python.
```python
exemplo_lista = [3, 2, 1, 'Carro', 'Porta']
```

### Tuplas

- **tuple**: Semelhantes a listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados depois de definidos. São definidas usando parênteses (). Por exemplo, no código abaixo há uma representação de uma tupla em Python.
```python
exemplo_tupla = (1, 2, 3, "quatro", 5.0)
```

### Dicionários

- **dict**: Coleção não ordenada de pares chave-valor, onde cada chave é única. Os valores podem ser de qualquer tipo de dado e são acessados através das chaves. Por exemplo, no código abaixo há uma representação de uma tupla em Python.
```python
exemplo_dicionario = {"nome": "Victor", "idade": 29, "cidade": "Bauru"}
```

Estes são os principais tipos de dados em Python que você encontrará frequentemente ao programar. Cada tipo de dado tem suas próprias características e métodos associados, tornando Python uma linguagem poderosa e flexível para lidar com uma variedade de situações de programação.


## Estruturas Condicionais em Python


As estruturas condicionais são utilizadas em Python para controlar o fluxo do programa com base em condições específicas. As estruturas condicionais mais comuns em Python são:

### If

O bloco `if` é usado para executar um bloco de código se uma condição for verdadeira.

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

### Else
O bloco `else` é usado junto com o `if` para executar um bloco de código quando a condição do `if` é falsa (valor lógico False do Python).

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

### Elif
O bloco `elif` é uma abreviação de "else if" e é usado para verificar múltiplas condições. Ele é colocado entre os blocos `if` e `else` e só é executado se a condição do `if` anterior for falsa.

```python
nota = 7

if nota >= 9:
    print("Aprovado com A.")
elif nota >= 8:
    print("Aprovado com B.")
elif nota >= 7:
    print("Aprovado com C.")
else:
    print("Reprovado.")
```

### Operadores Lógicos

Em Python, você pode combinar múltiplas condições usando operadores lógicos:

- `and`: Retorna True se ambas as condições forem verdadeiras.
- `or`: Retorna True se pelo menos uma das condições for verdadeira.
- `not`: Inverte o resultado da condição.

No código abaixo, há um exemplo em Python do uso do operador lógico `and`.

```python
idade = 25

if idade >= 18 and idade <= 65:
    print("Você é um adulto.")
```


## Estruturas de Repetição em Python

As estruturas de repetição são utilizadas em Python para executar um bloco de código várias vezes. Python oferece duas principais estruturas de repetição:

### While

O loop `while` é usado para executar um bloco de código repetidamente enquanto uma condição especificada for verdadeira. Abaixo, um código em Python utilizando `While`.

```python
contador = 0

while contador < 10:
    print(contador)
    contador += 1
```

### For

O loop `for` é usado para iterar sobre uma sequência (como listas, tuplas, strings, entre outros) ou outros objetos iteráveis. Abaixo, um código em Python utilizando `for`.

```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
```

### Break e Continue

- `break`: Encerra imediatamente o loop.
- `continue`: Pula para a próxima iteração do loop.

Abaixo, um exemplo de código em Python utilizando `break`para interromper o loop quando o valor de `i` for igual a 3.

```python
for i in range(10):
    if i == 3:
        break
    print(i)
```

Ainda, no código abaixo, um exemplo de código em Python utilizando `continue` para "pular" para a próxima iteração quando o valor de `i` for igual a 2. 

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### Else em Loops

A linguagem de programação Python permite usar a cláusula `else` em loops. O bloco de código no else é executado quando o loop é concluído sem ser interrompido pelo break.

Abaixo, um exemplo de código em Python utilizando `else` em loops.

```python
for i in range(3):
    print(i)
else:
    print("Loop concluído.")
```

## Tratamento de Exceções em Python

O tratamento de exceções em Python é uma técnica para lidar com erros e situações inesperadas que podem ocorrer durante a execução de um programa. Neste tutorial, vamos aprender como usar as declarações `try`, `except`, `else` e `finally` para lidar com exceções em Python.

### Sintaxe Básica

A estrutura básica do tratamento de exceções em Python é a seguinte:

```python
try:
    # Código que pode gerar exceções
    ...
except Excecao1:
    # Código para lidar com Excecao1
    ...
except Excecao2:
    # Código para lidar com Excecao2
    ...
else:
    # Código a ser executado se nenhuma exceção for levantada
    ...
finally:
    # Código a ser executado sempre, independentemente de exceções
    ...
```

Ainda, abaixo um exemplo de código em Python para tratamento de exceções.

```python
def dividir(a, b):
    try:
        resultado = a / b
        print("O resultado da divisão é:", resultado)
    except ZeroDivisionError:
        print("Ocorreu um erro. Motivo: Divisão por zero não é permitida.")
    except TypeError:
        print("Ocorreu um erro. Motivo: Certifique-se de que ambos os números são válidos.")

dividir(10, 2)   # Saída: O resultado da divisão é: 5.0
dividir(10, 0)   # Saída: Ocorreu um erro. Motivo: Divisão por zero não é permitida.
dividir("10", 2) # Saída: Ocorreu um erro. Motivo: Certifique-se de que ambos os números são válidos.
```

## Orientação a Objetos em Python

A orientação a objetos é um paradigma de programação que permite modelar problemas complexos de forma mais clara e organizada. Python é uma linguagem orientada a objetos, o que significa que tudo em Python é um objeto ou uma instância de uma classe. Neste tutorial, vamos aprender sobre classes, objetos, métodos, herança e outros conceitos importantes de orientação a objetos em Python.


### Classes e Objetos

Em Python, uma classe é uma estrutura que define o comportamento e as propriedades de um objeto. Um objeto é uma instância de uma classe. Abaixo, um exemplo de definição de classe em Python:


```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos.")

# Criando um objeto da classe Pessoa
obj_pessoa_1 = Pessoa("Victor", 29)

# Chamando o método apresentar do objeto
obj_pessoa_1.apresentar()  # Saída: Olá, meu nome é Victor e tenho 29 anos.
```

### Construtor (init)

O método `__init__` é um método especial usado para inicializar objetos quando são criados. Ele é chamado automaticamente quando você cria uma nova instância da classe. No código abaixo há um exemplo do método `__init__.py`.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

### Atributos

Os atributos são variáveis associadas a uma classe e são usados para armazenar dados sobre os objetos. Eles são acessados usando a notação de ponto.

No código abaixo, há um exemplo de um atributo criado em uma classe.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    # Atributo: nome
        self.idade = idade  # Atributo: idade

obj_pessoa_1 = Pessoa("Victor", 29)
print(obj_pessoa_1.nome)    # Saída do Atributo: Victor
```


### Métodos

Métodos são funções definidas dentro de uma classe e são usados para realizar operações nos objetos da classe.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

obj_pessoa_1 = Pessoa("Victor", 29)

# Chamando o método de instância
obj_pessoa_1.apresentar()  # Saída: Olá, meu nome é Victor e tenho 29 anos
```

### Encapsulamento

O encapsulamento é o conceito de ocultar os detalhes de implementação de um objeto e permitir o acesso controlado aos seus atributos e métodos.

### Polimorfismo

O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme, fornecendo uma interface comum para diferentes tipos de objetos.

