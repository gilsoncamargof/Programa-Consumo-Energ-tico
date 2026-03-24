# Calculadora de Consumo Elétrico
# Projeto de iniciação em tecnologia

TARIFA_KWH = 0.75  # R$ por kWh (valor médio estimado)

def exibir_banner():
    print("=" * 50)
    print("  ⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡")
    print("=" * 50)
    print()

def obter_dado_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("  ❌ Por favor, informe um valor válido.\n")

def obter_dado_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem).strip())
            if valor <= 0:
                print("  ❌ O valor deve ser maior que zero.\n")
            else:
                return valor
        except ValueError:
            print("  ❌ Por favor, informe um número válido.\n")

def calcular_consumo(potencia_w, horas_dia):
    """Fórmula: consumoMensal = (potencia * horasDia * 30) / 1000"""
    return (potencia_w * horas_dia * 30) / 1000

def classificar_consumo(kwh_mes):
    if kwh_mes < 10:
        return "🟢 Baixo consumo"
    elif kwh_mes < 50:
        return "🟡 Consumo moderado"
    else:
        return "🔴 Alto consumo"

def exibir_resultado(aparelho, potencia, horas_dia, consumo_mensal):
    custo_estimado = consumo_mensal * TARIFA_KWH
    classificacao = classificar_consumo(consumo_mensal)

    print()
    print("=" * 50)
    print("         📊 RESULTADO DO CÁLCULO")
    print("=" * 50)
    print(f"  Aparelho:           {aparelho}")
    print(f"  Potência:           {potencia:.0f} W")
    print(f"  Uso diário:         {horas_dia:.1f} horas/dia")
    print(f"  Consumo estimado:   {consumo_mensal:.2f} kWh/mês")
    print(f"  Custo estimado:     R$ {custo_estimado:.2f}/mês")
    print(f"  Classificação:      {classificacao}")
    print("=" * 50)
    print()

def perguntar_continuar():
    resposta = input("  🔄 Calcular outro aparelho? (s/n): ").strip().lower()
    return resposta in ("s", "sim", "y", "yes")

def main():
    exibir_banner()
    print("  📌 Calcule o consumo elétrico dos seus aparelhos")
    print(f"  💰 Tarifa utilizada: R$ {TARIFA_KWH}/kWh\n")

    while True:
        aparelho = obter_dado_texto("  🔌 Nome do aparelho: ")
        potencia = obter_dado_numero("  ⚡ Potência em watts (W): ")
        horas_dia = obter_dado_numero("  🕐 Horas de uso por dia: ")

        consumo = calcular_consumo(potencia, horas_dia)
        exibir_resultado(aparelho, potencia, horas_dia, consumo)

        if not perguntar_continuar():
            print()
            print("  ✅ Obrigado por usar a Calculadora de Consumo Elétrico!")
            print("  💡 Dica: Desligue aparelhos em stand-by para economizar energia.")
            print()
            break
        print()

if __name__ == "__main__":
    main()