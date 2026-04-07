class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def latir(self):
        return "auauau"

    def __str__(self):
        return f'Nome: {self.get_nome()}\nIdade: {self.get_idade()}\nFaz: {self.latir()}'