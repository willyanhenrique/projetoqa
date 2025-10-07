import pytest
from comparador import calcular_consorcio, calcular_financiamento

#Valor mínimo de R$ 10.000,00
@pytest.mark.parametrize(
    "valor, taxa, prazo",
    [
        (9000, 10, 60),   # valor abaixo do mínimo
        (9999.99, 5, 48), # valor pouco abaixo do limite
    ]
)
def test_valor_minimo_consorcio(valor, taxa, prazo):
    with pytest.raises(ValueError):
        calcular_consorcio(valor=valor, taxa_admin=taxa, prazo=prazo)


@pytest.mark.parametrize(
    "valor, juros, prazo",
    [
        (5000, 1.5, 36),
        (9999, 2, 24),
    ]
)
def test_valor_minimo_financiamento(valor, juros, prazo):
    with pytest.raises(ValueError):
        calcular_financiamento(valor=valor, juros_mensal=juros, prazo=prazo)


#Prazo máximo de 120 meses
@pytest.mark.parametrize(
    "valor, taxa, prazo",
    [
        (100000, 10, 121),  # ultrapassa o limite de 120 meses
        (50000, 5, 200),    # muito acima do limite
    ]
)
def test_prazo_maximo_consorcio(valor, taxa, prazo):
    with pytest.raises(ValueError):
        calcular_consorcio(valor=valor, taxa_admin=taxa, prazo=prazo)


@pytest.mark.parametrize(
    "valor, juros, prazo",
    [
        (100000, 1.2, 121),
        (75000, 1.5, 180),
    ]
)
def test_prazo_maximo_financiamento(valor, juros, prazo):
    with pytest.raises(ValueError):
        calcular_financiamento(valor=valor, juros_mensal=juros, prazo=prazo)