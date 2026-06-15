# Sprint 2- Soluções em Energias Renováveis e Sustentáveis

### Integrantes

| Nome                         | RM     |
| ---------------------------- | ------ |
| Matheus de Lara Silva        | 572935 |
| Gustavo Naville Tobara       | 570674 |
| Guilherme Marques dos Santos | 573112 |
| Guilherme Wadt de Oliveira   | 569375 |
| Pedro Henrique Silva Santos  | 571537 |

---

# Visão Geral

O ChargeGrid Intelligence é uma plataforma voltada ao gerenciamento inteligente da infraestrutura de recarga de veículos elétricos em ambientes comerciais.

A solução foi desenvolvida no contexto do EV Challenge 2026 e tem como objetivo otimizar o uso da energia elétrica através do controle de demanda, permitindo uma operação mais eficiente e sustentável dos eletropostos.

---

# Problema

O crescimento da mobilidade elétrica aumenta a demanda por infraestrutura de carregamento.

Em muitos cenários comerciais, a ausência de mecanismos inteligentes de gerenciamento pode provocar:

* Sobrecarga da rede elétrica;
* Picos de consumo;
* Desperdício energético;
* Aumento dos custos operacionais.

Além disso, a integração entre carregadores, sistemas de monitoramento e gestão energética ainda é limitada.

---

# Solução Proposta

A Prova de Conceito desenvolvida consiste em um sistema de controle inteligente de demanda.

O sistema monitora o consumo energético da instalação e ajusta automaticamente a potência destinada ao carregamento dos veículos elétricos.

Dessa forma, a infraestrutura opera dentro de limites seguros e energeticamente eficientes.

---

# Arquitetura

```text
Dados Simulados
       │
       ▼
Controle de Demanda
       │
       ▼
Motor de Decisão
       │
       ▼
Dashboard Streamlit
       │
       ▼
Visualização dos Resultados
```

---

# Funcionamento

O sistema utiliza três variáveis principais:

* Potência máxima disponível;
* Consumo atual da instalação;
* Potência solicitada pelo veículo.

### Regra de Controle

Potência disponível = Potência máxima − Consumo da instalação

Caso a potência solicitada seja superior à potência disponível, o sistema reduz automaticamente a potência de carregamento.

---

# Exemplo

| Variável            | Valor |
| ------------------- | ----- |
| Potência Máxima     | 30 kW |
| Consumo do Prédio   | 18 kW |
| Potência Solicitada | 22 kW |
| Potência Liberada   | 12 kW |

---

# Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* GitHub

---

# Sustentabilidade e Energias Renováveis

A solução foi fundamentada nos conceitos estudados na disciplina de Soluções em Energias Renováveis e Sustentáveis.

Os principais benefícios são:

## Eficiência Energética

O sistema evita desperdícios e otimiza a utilização da infraestrutura elétrica.

## Gestão Inteligente da Demanda

O controle automático reduz picos de consumo e melhora a estabilidade energética.

## Integração Futura com Fontes Renováveis

A arquitetura foi concebida para futura integração com sistemas fotovoltaicos e carregadores inteligentes.

## Mobilidade Sustentável

Ao otimizar o carregamento de veículos elétricos, a solução contribui para uma matriz de transporte mais limpa e eficiente.

---

# Resultados da Prova de Conceito

A PoC demonstrou que é possível:

* Monitorar variáveis energéticas;
* Aplicar regras automáticas de controle;
* Ajustar dinamicamente a potência de carregamento;
* Melhorar a eficiência operacional da infraestrutura.

---

# Trabalhos Futuros

* Integração com carregadores GoodWe;
* Comunicação via Modbus TCP;
* Tarifação dinâmica;
* Registro completo de sessões de carregamento;
* Aplicação de Inteligência Artificial para previsão de demanda;
* Integração futura com OCPP.

---

# Vídeo Demonstrativo

Inserir link do vídeo.

---

# Repositório

Inserir link do GitHub.
