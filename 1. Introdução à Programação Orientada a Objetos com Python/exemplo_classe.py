
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    

if __name__ == "__main__":
    pessoa1 = Pessoa("Elvio", 275)
    pessoa2 = Pessoa("Victor", 31)

    print(pessoa1.apresentar())
    print(pessoa2.apresentar())