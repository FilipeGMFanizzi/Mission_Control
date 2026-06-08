# Mission Control AI

Sistema de monitoramento de missão espacial desenvolvido em Python para a Global Solution 2026.1 da FIAP.

## O que o projeto faz

O programa simula o monitoramento de uma missão espacial chamada **Nova Frontier Alpha**. Ele analisa 6 ciclos de monitoramento e verifica se a missão está estável, em atenção ou em situação crítica.

Em cada ciclo são analisados:
- Temperatura interna do módulo
- Qualidade da comunicação com a base
- Nível de bateria
- Nível de oxigênio
- Estabilidade operacional

No final o programa gera um relatório completo com médias, tendência da missão e a área que acumulou mais risco.

## Como rodar

Só precisa ter o Python instalado. Não usa nenhuma biblioteca externa.

```
python mission_control.py
```

## Regras de alerta

### Temperatura
- Abaixo de 18°C: ATENCAO
- Entre 18°C e 30°C: NORMAL
- Entre 31°C e 35°C: ATENCAO
- Acima de 35°C: CRITICO

### Comunicação
- Abaixo de 30%: CRITICO
- Entre 30% e 59%: ATENCAO
- 60% ou mais: NORMAL

### Bateria
- Abaixo de 20%: CRITICO
- Entre 20% e 49%: ATENCAO
- 50% ou mais: NORMAL

### Oxigênio
- Abaixo de 80%: CRITICO
- Entre 80% e 89%: ATENCAO
- 90% ou mais: NORMAL

### Estabilidade
- Abaixo de 40%: CRITICO
- Entre 40% e 69%: ATENCAO
- 70% ou mais: NORMAL

## Pontuação de risco

Cada classificação gera uma pontuação por ciclo:
- NORMAL = 0 ponto
- ATENCAO = 1 ponto
- CRITICO = 2 pontos

A pontuação máxima por ciclo é 10 (5 áreas x 2 pontos cada).

Com base na pontuação total o ciclo é classificado assim:
- 0 a 2 pontos: MISSAO ESTAVEL
- 3 a 5 pontos: MISSAO EM ATENCAO
- 6 a 10 pontos: MISSAO CRITICA

## Funções do projeto

- `analisar_temperatura()` - classifica a temperatura do ciclo
- `analisar_comunicacao()` - classifica a comunicação do ciclo
- `analisar_bateria()` - classifica a bateria do ciclo
- `analisar_oxigenio()` - classifica o oxigênio do ciclo
- `analisar_estabilidade()` - classifica a estabilidade do ciclo
- `classificar_ciclo()` - define se o ciclo é estável, em atenção ou crítico
- `analisar_tendencia()` - compara o primeiro e o último ciclo para ver se a missão melhorou ou piorou
- `identificar_area_mais_afetada()` - soma os pontos de risco por área e retorna a mais afetada
- `gerar_recomendacao()` - gera uma recomendação com base nos alertas do ciclo

## Estrutura do repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

## Equipe

Equipe Cosmos - FIAP 2026
