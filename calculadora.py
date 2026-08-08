CUPONS_PERCENTUAIS = {
    "DEVOPS10": 10,
    "BOASVINDAS5": 5,
}


def obter_desconto_do_cupom(cupom):
    """
    Retorna o percentual de desconto associado a um cupom.
    Se o cupom for None, não há desconto (0%).
    """
    if cupom is None:
        return 0

    codigo = cupom.strip().upper()
    if codigo not in CUPONS_PERCENTUAIS:
        raise ValueError("Cupom promocional inválido.")

    return CUPONS_PERCENTUAIS[codigo]


def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)

    O desconto pode vir de um percentual direto (desconto_percentual)
    ou de um cupom promocional (cupom).
    """
    if cupom is not None:
        desconto_percentual = obter_desconto_do_cupom(cupom)

    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    total = subtotal - (subtotal * desconto_percentual / 100)

    return round(total, 2)

def test_cupom_devops10_funciona_com_minusculas():
    itens = [(200.0, 1)]
    assert calcular_total(itens, cupom="devops10") == 180.0


def test_cupom_soma_com_descontos_existente():
    itens = [(100.0, 1)]
    total = calcular_total(itens, desconto_percentual=5, cupom="DEVOPS10")
    assert total == 85.0

def test_cupom_invalido_gera_erro():
    itens = [(100.0, 1)]
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], cupom="XPTO")




