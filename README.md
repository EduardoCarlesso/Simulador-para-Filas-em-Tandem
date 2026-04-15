# 📊 Relatório de Simulação de Filas em Tandem

## 1. Descrição do Sistema Simulado

O sistema simulado consiste em duas filas em tandem. A Fila 1 recebe clientes do ambiente externo e, após o atendimento, estes são encaminhados para a Fila 2. Após o atendimento na Fila 2, os clientes deixam o sistema.

A simulação foi realizada por meio da técnica de **Simulação de Eventos Discretos (SED)**.

---

## 2. Parâmetros da Simulação

### 🔹 Fila 1 – G/G/2/3
- **Intervalo de chegada:** 1 a 4 unidades de tempo  
- **Intervalo de atendimento:** 3 a 4 unidades de tempo  
- **Número de servidores:** 2  
- **Capacidade do sistema:** 3 clientes  

### 🔹 Fila 2 – G/G/1/5
- **Intervalo de atendimento:** 2 a 3 unidades de tempo  
- **Número de servidores:** 1  
- **Capacidade do sistema:** 5 clientes  

### 🔹 Configurações Gerais
- **Primeira chegada:** t = 1,5  
- **Estado inicial:** Filas vazias  
- **Limite de números aleatórios:** 100.000  

---

## 3. Resultados da Simulação

### 🔹 Fila 1 – G/G/2/3

| Estado | Tempo Acumulado | Probabilidade |
|--------|-----------------|---------------|
| 0 | 1646.5783 | 0.019634 |
| 1 | 47123.0135 | 0.561910 |
| 2 | 32379.0378 | 0.386098 |
| 3 | 2713.6485 | 0.032358 |

**Perdas:** 78

---

### 🔹 Fila 2 – G/G/1/5

| Estado | Tempo Acumulado | Probabilidade |
|--------|-----------------|---------------|
| 0 | 1424.2812 | 0.016984 |
| 1 | 14733.9361 | 0.175692 |
| 2 | 21905.1660 | 0.261204 |
| 3 | 21091.7542 | 0.251505 |
| 4 | 18953.1505 | 0.226003 |
| 5 | 5753.9902 | 0.068612 |

**Perdas:** 520

---

## 4. Estatísticas Globais

| Métrica | Valor |
|---------|-------|
| **Tempo Global da Simulação** | 83.862,2782 |
| **Número de Aleatórios Utilizados** | 100.000 |

---

## 5. Conclusão

Os resultados obtidos demonstram que a simulação foi executada corretamente, atendendo a todos os requisitos propostos. A distribuição de probabilidades, os tempos acumulados em cada estado, o número de perdas e o tempo global foram devidamente calculados.

O modelo representa adequadamente uma rede de filas em tandem, validando a implementação do simulador e garantindo a consistência dos resultados obtidos.

---
