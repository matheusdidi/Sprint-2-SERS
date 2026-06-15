# Sprint 2- Soluções em Energias Renováveis e Sustentáveis

### Integrantes

| Nome                         | RM     |
| ---------------------------- | ------ |
| Matheus de Lara Silva        | 57293 |
| Gustavo Naville Tobara       | 570674 |
| Guilherme Marques dos Santos | 573112 |
| Guilherme Wadt de Oliveira   | 569375 |
| Pedro Henrique Silva Santos  | 571537 |

---

# 📋 Visão Geral

O ChargeGrid Intelligence é uma solução desenvolvida para o EV Challenge 2026 com o objetivo de otimizar a gestão energética de eletropostos comerciais.

A proposta consiste em um sistema inteligente de controle de demanda capaz de monitorar o consumo energético de uma instalação e ajustar automaticamente a potência disponibilizada para o carregamento de veículos elétricos.

Nesta Sprint 2 foi desenvolvida uma Prova de Conceito (PoC) funcional baseada em simulação, validando a lógica de gerenciamento energético da solução.

---

# 🚨 Problema

Com o crescimento da mobilidade elétrica, aumenta também a necessidade de infraestrutura de recarga eficiente e sustentável.

Em muitos estabelecimentos comerciais, os carregadores de veículos elétricos compartilham a mesma rede elétrica utilizada por outros equipamentos da instalação. Sem um mecanismo inteligente de gerenciamento, podem ocorrer:

* Sobrecarga da infraestrutura elétrica;
* Picos de demanda;
* Desperdício energético;
* Aumento dos custos operacionais;
* Necessidade de expansão da rede elétrica.

Além disso, muitos eletropostos ainda não possuem integração entre monitoramento energético, controle de potência e gestão operacional.

---

# 💡 Solução Proposta

O trabalho utiliza um sistema de controle de demanda para distribuir a potência elétrica disponível de forma inteligente.

A solução monitora:

* Potência máxima da instalação;
* Consumo atual do estabelecimento;
* Potência solicitada pelo veículo elétrico.

A partir desses dados, o sistema calcula automaticamente a potência disponível para carregamento.

Quando a potência solicitada pelo veículo ultrapassa a capacidade disponível da instalação, o sistema reduz automaticamente a potência liberada ao carregador, evitando sobrecargas e garantindo uma operação mais eficiente.

---

# 🏗 Arquitetura da Solução

```text
Usuário
   │
   ▼
Dashboard Streamlit
   │
   ▼
Motor de Controle de Demanda
   │
   ├── Potência Máxima da Instalação
   ├── Consumo Atual do Prédio
   └── Potência Solicitada pelo Veículo
   │
   ▼
Cálculo da Potência Disponível
   │
   ▼
Decisão Automática
   │
   ▼
Potência Liberada ao Carregador
```

---

# ⚙️ Funcionamento

A lógica da Prova de Conceito é baseada na seguinte regra:

```text
Potência Disponível =
Potência Máxima da Instalação
−
Consumo Atual do Prédio
```

Se:

```text
Potência Solicitada > Potência Disponível
```

então:

```text
Potência Liberada = Potência Disponível
```

Caso contrário:

```text
Potência Liberada = Potência Solicitada
```

---

# 📊 Exemplo de Simulação

| Variável                         | Valor |
| -------------------------------- | ----- |
| Potência Máxima                  | 30 kW |
| Consumo do Prédio                | 18 kW |
| Potência Solicitada pelo Veículo | 22 kW |
| Potência Disponível              | 12 kW |
| Potência Liberada                | 12 kW |

Resultado:

O sistema identifica a insuficiência de potência e reduz automaticamente o carregamento para evitar sobrecarga da instalação.

---

# 🖥️ Prova de Conceito Desenvolvida

A PoC foi implementada utilizando um dashboard interativo desenvolvido em Python.

O sistema permite:

* Simular diferentes cenários de consumo;
* Alterar a potência máxima da instalação;
* Alterar a potência solicitada pelo veículo;
* Visualizar o acionamento do controle de demanda;
* Visualizar os resultados em tempo real;
* Exibir gráficos de distribuição de potência.

---

# 🛠 Tecnologias Utilizadas

* Python 3.14
* Streamlit
* Pandas
* Plotly
* GitHub

---

# 🌱 Sustentabilidade e Eficiência Energética

A solução foi desenvolvida com base nos conceitos estudados na disciplina de Soluções em Energias Renováveis e Sustentáveis.

Os principais benefícios são:

### Eficiência Energética

Utilização otimizada da infraestrutura elétrica existente, reduzindo desperdícios e aumentando a eficiência operacional.

### Gestão Inteligente da Demanda

Redução de picos de consumo e melhor distribuição da energia disponível.

### Mobilidade Sustentável

Contribuição para a expansão segura e eficiente da infraestrutura de recarga de veículos elétricos.

### Integração com Energias Renováveis

A arquitetura foi concebida para futura integração com sistemas fotovoltaicos e soluções energéticas do ecossistema GoodWe.

---

# 📷 Evidências

<img width="1844" height="901" alt="Captura de tela 2026-06-15 165139" src="https://github.com/user-attachments/assets/b23ff526-9bd8-403f-99a4-1809585e3dd1" />
<img width="1850" height="902" alt="Captura de tela 2026-06-15 165326" src="https://github.com/user-attachments/assets/1e03666d-525c-47c1-9726-e820b2753c84" />
