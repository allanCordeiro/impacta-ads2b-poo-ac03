import loja


def testa_produto():
    produto = loja.Produto('PC', 1500)
    print(produto.nome)
    print(produto.preco)
    print(produto.calcular_preco_com_frete())

def testa_produto_fisico():
    produto_fisico = loja.ProdutoFisico('PC', 100, 1000)
    print(produto_fisico.nome)
    print(produto_fisico.peso)
    print(produto_fisico.preco)
    print(produto_fisico.peso_em_kg())
    print(produto_fisico.calcular_preco_com_frete())

def testa_produto_eletronico():
    produto_eletronico = loja.ProdutoEletronico('PC', 100, 1000, 220, 4)
    print(produto_eletronico.nome)
    print(produto_eletronico.tensao)
    print(produto_eletronico.tempo_garantia)
    print(produto_eletronico.calcular_preco_com_frete())

def testa_ebook():
    ebook = loja.Ebook("Aprendendo Python", 30, "Allan Cordeiro", 300)
    print(ebook.nome_exibicao)
    print(ebook.preco)
    print(ebook.numero_paginas)
    print(ebook.calcular_preco_com_frete())

if __name__ == "__main__":
    print("testando classe Loja")
    testa_produto()
    print("*" * 60)
    print("testando classe ProdutoFisico")
    testa_produto_fisico()
    print("*" * 60)
    print("testando classe ProdutoEletronico")
    testa_produto_eletronico()
    print("*" * 60)
    print("testando classe Ebook")
    testa_ebook()
    print("*" * 60)
