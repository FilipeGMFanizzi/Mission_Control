# Mission Control AI
# GS2026.1 - Pensamento Computacional e Automação em Python
# Missão: Nova Frontier Alpha
# Equipe: Equipe Cosmos

nome_missao = "Nova Frontier Alpha"
nome_equipe = "Equipe Cosmos"

dados_missao = [
    [23, 95, 91, 97, 92],
    [26, 83, 75, 95, 86],
    [32, 67, 60, 92, 71],
    [37, 44, 35, 85, 52],
    [40, 25, 17, 76, 33],
    [35, 58, 30, 81, 48]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]


def analisar_temperatura(temp):
    if temp < 18:
        return "ATENCAO", 1, "Temperatura baixa"
    elif temp <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif temp <= 35:
        return "ATENCAO", 1, "Temperatura elevada"
    else:
        return "CRITICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(com):
    if com < 30:
        return "CRITICO", 2, "Comunicacao em nivel critico"
    elif com < 60:
        return "ATENCAO", 1, "Comunicacao instavel"
    else:
        return "NORMAL", 0, "Comunicacao estavel"


def analisar_bateria(bat):
    if bat < 20:
        return "CRITICO", 2, "Bateria em nivel critico"
    elif bat < 50:
        return "ATENCAO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estavel"


def analisar_oxigenio(oxi):
    if oxi < 80:
        return "CRITICO", 2, "Oxigenio em nivel critico"
    elif oxi < 90:
        return "ATENCAO", 1, "Oxigenio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigenio adequado"


def analisar_estabilidade(est):
    if est < 40:
        return "CRITICO", 2, "Estabilidade critica"
    elif est < 70:
        return "ATENCAO", 1, "Estabilidade reduzida"
    else:
        return "NORMAL", 0, "Estabilidade adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missao apresentou tendencia de piora."
    elif riscos[-1] < riscos[0]:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."


def identificar_area_mais_afetada(pontos_por_area):
    maior = 0
    indice = 0
    for i in range(len(pontos_por_area)):
        if pontos_por_area[i] > maior:
            maior = pontos_por_area[i]
            indice = i
    return areas_monitoradas[indice], maior


def gerar_recomendacao(r_temp, r_com, r_bat, r_oxi, r_est):
    recomendacoes = []

    if r_temp[0] == "CRITICO":
        recomendacoes.append("verificar controle termico da missao")
    if r_com[0] == "CRITICO":
        recomendacoes.append("tentar restabelecer contato com a base")
    if r_bat[0] == "CRITICO":
        recomendacoes.append("ativar modo de economia de energia")
    if r_oxi[0] == "CRITICO":
        recomendacoes.append("acionar protocolo de suporte a vida")
    if r_est[0] == "CRITICO":
        recomendacoes.append("reduzir operacoes nao essenciais")

    if len(recomendacoes) >= 3:
        return "Ativar modo de seguranca e priorizar suporte a vida, energia e comunicacao."
    elif len(recomendacoes) > 0:
        return "Acoes necessarias: " + ", ".join(recomendacoes) + "."
    else:
        return "Manter operacao normal e continuar monitoramento."


# inicio do programa
print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missao:", nome_missao)
print("Equipe:", nome_equipe)
print("Quantidade de ciclos analisados:", len(dados_missao))
print("=" * 60)

riscos = []
pontos_por_area = [0, 0, 0, 0, 0]

for i in range(len(dados_missao)):
    ciclo = dados_missao[i]

    temp = ciclo[0]
    com  = ciclo[1]
    bat  = ciclo[2]
    oxi  = ciclo[3]
    est  = ciclo[4]

    r_temp = analisar_temperatura(temp)
    r_com  = analisar_comunicacao(com)
    r_bat  = analisar_bateria(bat)
    r_oxi  = analisar_oxigenio(oxi)
    r_est  = analisar_estabilidade(est)

    pontuacao = r_temp[1] + r_com[1] + r_bat[1] + r_oxi[1] + r_est[1]
    classificacao = classificar_ciclo(pontuacao)
    recomendacao = gerar_recomendacao(r_temp, r_com, r_bat, r_oxi, r_est)

    pontos_por_area[0] = pontos_por_area[0] + r_temp[1]
    pontos_por_area[1] = pontos_por_area[1] + r_com[1]
    pontos_por_area[2] = pontos_por_area[2] + r_bat[1]
    pontos_por_area[3] = pontos_por_area[3] + r_oxi[1]
    pontos_por_area[4] = pontos_por_area[4] + r_est[1]

    riscos.append(pontuacao)

    print("\nCICLO", i + 1)
    print("-" * 60)
    print("Temperatura:", temp, "C |", r_temp[0], "|", r_temp[2])
    print("Comunicacao:", com, "% |", r_com[0], "|", r_com[2])
    print("Bateria:", bat, "% |", r_bat[0], "|", r_bat[2])
    print("Oxigenio:", oxi, "% |", r_oxi[0], "|", r_oxi[2])
    print("Estabilidade:", est, "% |", r_est[0], "|", r_est[2])
    print("Pontuacao de risco do ciclo:", pontuacao)
    print("Classificacao do ciclo:", classificacao)
    print("Recomendacao:", recomendacao)

# relatorio final
area_afetada, pts_area = identificar_area_mais_afetada(pontos_por_area)
tendencia = analisar_tendencia(riscos)

total_temp = 0
total_com  = 0
total_bat  = 0
total_oxi  = 0
total_est  = 0

for ciclo in dados_missao:
    total_temp = total_temp + ciclo[0]
    total_com  = total_com  + ciclo[1]
    total_bat  = total_bat  + ciclo[2]
    total_oxi  = total_oxi  + ciclo[3]
    total_est  = total_est  + ciclo[4]

n = len(dados_missao)
media_temp = total_temp / n
media_com  = total_com  / n
media_bat  = total_bat  / n
media_oxi  = total_oxi  / n
media_est  = total_est  / n

maior_risco = riscos[0]
ciclo_critico = 1
for i in range(len(riscos)):
    if riscos[i] > maior_risco:
        maior_risco = riscos[i]
        ciclo_critico = i + 1

risco_medio = sum(riscos) / n

ciclos_criticos = 0
for r in riscos:
    if r >= 6:
        ciclos_criticos = ciclos_criticos + 1

classif_final = classificar_ciclo(round(risco_medio))

print("\n" + "=" * 60)
print("RELATORIO FINAL DA MISSAO")
print("=" * 60)
print("Missao:", nome_missao)
print("Equipe:", nome_equipe)
print("Quantidade de ciclos analisados:", n)
print("\nMedia de temperatura:", round(media_temp, 2), "C")
print("Media de comunicacao:", round(media_com, 2), "%")
print("Media de bateria:", round(media_bat, 2), "%")
print("Media de oxigenio:", round(media_oxi, 2), "%")
print("Media de estabilidade:", round(media_est, 2), "%")
print("\nCiclo mais critico: Ciclo", ciclo_critico)
print("Maior pontuacao de risco:", maior_risco)
print("Risco medio da missao:", round(risco_medio, 2))
print("Quantidade de ciclos criticos:", ciclos_criticos)
print("\nTendencia da missao:")
print(tendencia)
print("\nPontuacao acumulada por area:")
for i in range(len(areas_monitoradas)):
    print(areas_monitoradas[i] + ":", pontos_por_area[i], "pontos")
print("\nArea mais afetada:")
print(area_afetada, "-", pts_area, "pontos")
print("\nClassificacao final da missao:")
print(classif_final)
print("\nConclusao:")
if classif_final == "MISSAO CRITICA":
    print("A missao enfrentou situacoes criticas. E necessario acionar os protocolos de emergencia.")
elif classif_final == "MISSAO EM ATENCAO":
    print("A missao apresentou instabilidade. A equipe deve manter o plano de contingencia ativo.")
else:
    print("A missao transcorreu dentro dos parametros normais. Continuar monitoramento.")
print("=" * 60)
