import loja


def testa_produto():
    produto = loja.Produto('PC', 1.500)
    print(produto.nome)
    print(produto.preco)
    print(produto.calcular_preco_com_frete())

def testa_produto_fisico():
    produto_fisico = loja.ProdutoFisico('PC', 1500, 2)
    print(produto_fisico.nome)
    print(produto_fisico.peso)
    print(produto_fisico.preco)
    print(produto_fisico.peso_em_kg())
    print(produto_fisico.calcular_preco_com_frete())


if __name__ == "__main__":
    print("testando classe Loja")
    testa_produto()
    print("*" * 60)
    print("testando classe ProdutoFisico")
    testa_produto_fisico()
    print("*" * 60)

