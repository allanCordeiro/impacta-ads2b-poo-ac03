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
        if Utils.is_int(novo_preco) or isinstance(novo_preco, float):
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
        if Utils.is_int(novo_peso):
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


class ProdutoEletronico(ProdutoFisico):
    def __init__(self, nome, preco, peso, tensao, tempo_garantia):
        super().__init__(nome, preco, peso)
        self.__tensao = self.tensao = tensao
        self.__tempo_garantia = tempo_garantia

    @property
    def tensao(self):
        return self.__tensao

    @property
    def tempo_garantia(self):
        return self.__tempo_garantia

    @tensao.setter
    def tensao(self, nova_tensao):
        if Utils.is_int(nova_tensao):
            if nova_tensao == 0 or nova_tensao == 127 or nova_tensao == 220:
                self.__tensao = nova_tensao
            else:
                raise ValueError("'tensao' valor inválido.")
        else:
            raise TypeError("'tensao' deve ser um valor inteiro")

    def calcular_preco_com_frete(self):
        valor_frete = super(ProdutoEletronico, self).calcular_preco_com_frete()
        return valor_frete + (valor_frete * 0.01)


class Utils:
    # bool é subtipo de int. Se o test colocar True ou False, somente a validação por int vai falhar
    # pra ficar menos poluida a tela, um metodo já faz essa dupla validacao antes.
    @staticmethod
    def is_int(var_type):
        if not isinstance(var_type, bool) and isinstance(var_type, int):
            return True
        return False
