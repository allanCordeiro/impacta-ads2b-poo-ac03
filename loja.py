# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
# Allan Cordeiro dos Santos
# Email Impacta: allan.cordeiro@aluno.faculdadeimpacta.com.br

class Produto:
    def __init__(self, nome, preco):
        self.__nome = self.nome = nome
        self.__preco = self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) != 0:
            self.__nome = novo_nome
        else:
            raise ValueError("'nome' nao deve ser vazio.")

    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, bool) and isinstance(novo_preco, int) or isinstance(novo_preco, float):
            if novo_preco > 0:
                self.__preco = novo_preco
            else:
                raise ValueError("'preco' deve ser maior que zero.")
        else:
            raise TypeError("'preco' somente valores numericos sao aceitos")

    def calcular_preco_com_frete(self):
        return self.preco


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.__peso = self.peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        if not isinstance(novo_peso, bool) and isinstance(novo_peso, int):
            if novo_peso > 0:
                self.__peso = novo_peso
            else:
                raise ValueError("'peso' deve ser maior que zero")
        else:
            raise TypeError("'peso' deve ser um valor inteiro")

    def peso_em_kg(self):
        return self.peso / 1000

    def calcular_preco_com_frete(self):
        valor_por_kg = 5.0
        return self.preco + (self.peso_em_kg() * valor_por_kg)


