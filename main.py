print("=== ChargeGrid Intelligence ===")

potencia_maxima = 30

consumo_predio = float(
    input("Consumo atual do prédio (kW): ")
)

potencia_solicitada = float(
    input("Potência solicitada pelo veículo (kW): ")
)

potencia_disponivel = (
    potencia_maxima - consumo_predio
)

if potencia_solicitada > potencia_disponivel:
    potencia_liberada = potencia_disponivel

    print("\n⚠ Controle de demanda ativado!")

else:
    potencia_liberada = potencia_solicitada

    print("\n✅ Carregamento normal")

print(f"\nPotência disponível: {potencia_disponivel} kW")
print(f"Potência liberada: {potencia_liberada} kW")