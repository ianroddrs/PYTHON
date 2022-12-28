

class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
    
    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    def dar_like(self):
        self.__likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def __str__(self):
        return f"{self.nome} - {self.ano} : {self.likes} Likes"


class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min : {self.likes} Likes"

class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temp : {self.likes} Likes"


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()


# print(f"{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} : {vingadores.likes}")
# print(f"{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} : {atlanta.likes}")

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)