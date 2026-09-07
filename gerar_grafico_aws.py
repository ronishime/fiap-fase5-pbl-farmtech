# -*- coding: utf-8 -*-
"""Gera o gráfico de comparação de custos AWS (Entrega 2) a partir dos valores
cotados na Calculadora de Preços da AWS em 06/09/2026 (On-Demand 100%, Linux,
730 h/mês, volume EBS gp3 de 50 GB). Saída: assets/aws_comparacao_custos.png"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HORAS_MES = 730                                   # horas consideradas pela calculadora em 1 mês
GB = 50                                           # armazenamento exigido (GB)
REGIOES = ["Norte da Virgínia\n(us-east-1)", "São Paulo\n(sa-east-1)"]
PRECO_HORA = {"t3.micro": (0.0104, 0.0168),       # US$/hora (N. Virgínia, São Paulo)
              "t3a.micro": (0.0094, 0.0151),
              "t4g.micro": (0.0084, 0.0134)}
PRECO_GB = (0.080, 0.152)                         # US$/GB-mês do EBS gp3 (N. Virgínia, São Paulo)

ec2 = [p * HORAS_MES for p in PRECO_HORA["t3.micro"]]     # custo mensal da instância principal
ebs = [p * GB for p in PRECO_GB]                          # custo mensal do volume
totais = [round(a + b, 2) for a, b in zip(ec2, ebs)]      # totais como exibidos pela calculadora
fmt = lambda v: f"{v:.2f}".replace(".", ",")                 # formato decimal pt-BR

# Paleta e tokens (superfície clara)
AZUL, LARANJA, AQUA, VIOLETA = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
SUPERFICIE, INK, INK2, MUTED, GRID, BASE = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"

plt.rcParams.update({"font.family": "DejaVu Sans", "axes.edgecolor": BASE, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": MUTED, "text.color": INK})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2), facecolor=SUPERFICIE)
for ax in (ax1, ax2):
    ax.set_facecolor(SUPERFICIE)
    ax.grid(axis="y", color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    for lado in ("top", "right", "left"): ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)

# --- Painel A: custo mensal por região, empilhado por componente
x = [0, 1]; largura = 0.42; folga = 0.06                      # folga = espaço de 2px entre segmentos
ax1.bar(x, ec2, largura, color=AZUL, edgecolor=SUPERFICIE, linewidth=2)
ax1.bar(x, ebs, largura, bottom=[v + folga for v in ec2], color=LARANJA, edgecolor=SUPERFICIE, linewidth=2)
for i in x:
    ax1.text(i, ec2[i] / 2, f"EC2 t3.micro\nUS$ {fmt(ec2[i])}", ha="center", va="center", color="white", fontsize=9.5)
    ax1.text(i, ec2[i] + folga + ebs[i] / 2, f"EBS 50 GB\nUS$ {fmt(ebs[i])}", ha="center", va="center", color="white", fontsize=9.5)
    ax1.text(i, totais[i] + 0.5, f"US$ {fmt(totais[i])}/mês", ha="center", va="bottom", fontsize=12, fontweight="bold", color=INK)
dif = round(totais[1] - totais[0], 2)
ax1.annotate("", xy=(1, totais[1] + 2.6), xytext=(0, totais[0] + 2.6),
             arrowprops=dict(arrowstyle="->", color=INK2, lw=1.2))                      # seta N. Virgínia -> São Paulo
pct = f"{100 * dif / totais[0]:.1f}".replace(".", ",")                                  # diferença percentual
ax1.text(0.5, 15.0, f"+US$ {fmt(dif)}/mês (+{pct}%)\n+US$ {fmt(12 * dif)}/ano",
         ha="center", va="bottom", fontsize=10, color=INK2)                             # rótulo da diferença
ax1.set_xticks(x, REGIOES); ax1.set_ylim(0, totais[1] + 7.5)
ax1.set_ylabel("Custo mensal (US$)")
ax1.set_title("Máquina Linux 2 vCPU · 1 GiB · até 5 Gigabit · 50 GB\nOn-Demand 100% – custo mensal por região", fontsize=11, loc="left")
ax1.legend(handles=[Patch(color=AZUL, label="Instância EC2 t3.micro (730 h)"), Patch(color=LARANJA, label="Volume EBS gp3 (50 GB)")],
           loc="upper left", frameon=False, fontsize=9)

# --- Painel B: alternativas com a mesma especificação
inst = list(PRECO_HORA)
tot_nv = [PRECO_HORA[i][0] * HORAS_MES + ebs[0] for i in inst]
tot_sp = [PRECO_HORA[i][1] * HORAS_MES + ebs[1] for i in inst]
xi = range(len(inst)); w = 0.36
b1 = ax2.bar([v - w / 2 - 0.01 for v in xi], tot_nv, w, color=AQUA, edgecolor=SUPERFICIE, linewidth=2, label="Norte da Virgínia")
b2 = ax2.bar([v + w / 2 + 0.01 for v in xi], tot_sp, w, color=VIOLETA, edgecolor=SUPERFICIE, linewidth=2, label="São Paulo")
for barras in (b1, b2):
    for b in barras:
        ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.3, fmt(b.get_height()), ha="center", va="bottom", fontsize=9.5, color=INK)
ax2.set_xticks(list(xi), [f"{i}\n({'Intel' if i == 't3.micro' else 'AMD' if i == 't3a.micro' else 'ARM Graviton'})" for i in inst])
ax2.set_ylim(0, max(tot_sp) + 5); ax2.set_ylabel("Custo mensal total (US$)")
ax2.set_title("Instâncias que atendem à mesma especificação\n(instância + 50 GB gp3, On-Demand 100%)", fontsize=11, loc="left")
ax2.legend(loc="upper right", frameon=False, fontsize=9)

fig.text(0.01, 0.01, "Fonte: AWS Pricing Calculator (calculator.aws), cotação de 06/09/2026, Linux, locação compartilhada, sem transferência de dados nem snapshots.",
         fontsize=8, color=MUTED)
plt.tight_layout(rect=(0, 0.03, 1, 1))
Path("assets").mkdir(exist_ok=True)
fig.savefig("assets/aws_comparacao_custos.png", dpi=150, facecolor=SUPERFICIE, bbox_inches="tight")
print("gráfico salvo em assets/aws_comparacao_custos.png | totais:", [round(t, 2) for t in totais])
