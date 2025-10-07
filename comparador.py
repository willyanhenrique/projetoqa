def calcular_consorcio(valor, taxa_admin, prazo, reajuste_anual=5):
    if valor <= 0 or taxa_admin < 0 or prazo <= 0:
        raise ValueError("Valores inválidos para o cálculo do consórcio.")
    if valor < 10000:
        raise ValueError("O valor mínimo para o consórcio é de R$10.000,00.")
    if prazo > 120:
        raise ValueError("O prazo máximo permitido para consórcio é de 120 meses.")

    taxa = taxa_admin / 100
    parcela_base = (valor * (1 + taxa)) / prazo

    total = 0
    parcelas = []

    for mes in range(1, prazo + 1):
        anos_passados = (mes - 1) // 12
        fator_reajuste = (1 + reajuste_anual / 100)  
        parcela_corrigida = parcela_base * fator_reajuste

        parcelas.append(parcela_corrigida)
        total += parcela_corrigida

    return parcelas, total


def calcular_financiamento(valor, juros_mensal, prazo):
    if valor <= 0 or juros_mensal < 0 or prazo <= 0:
        raise ValueError("Valores inválidos para o cálculo do financiamento.")
    if valor < 10000:
        raise ValueError("O valor mínimo para financiamento é de R$10.000,00.")
    if prazo > 120:
        raise ValueError("O prazo máximo permitido para financiamento é de 120 meses.")

    i = juros_mensal / 100
    parcela = valor * (i * (1 + i) ** prazo) / ((1 + i) ** prazo - 1)
    total = parcela * prazo
    return parcela, total

