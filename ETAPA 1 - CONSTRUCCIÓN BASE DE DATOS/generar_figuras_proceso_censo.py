"""
Figuras metodológicas para tesis de maestría
Estilo: académico limpio, consistente, diferenciado por figura
Requisitos: 300 dpi, PNG, matplotlib puro
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
from pathlib import Path
import numpy as np

OUT = Path("figuras_tesis")
OUT.mkdir(exist_ok=True)

# ─────────────────────────────────────────────
# SISTEMA DE DISEÑO COMPARTIDO
# ─────────────────────────────────────────────
# Paleta
BG          = "#FAFAFA"
WHITE       = "#FFFFFF"
INK         = "#0F172A"        # texto principal
MUTED       = "#64748B"        # texto secundario
RULE        = "#CBD5E1"        # líneas divisoras

# Colores de acento por figura (cada una tiene identidad propia)
# Fig1: azul académico
F1_DARK     = "#1E3A5F"
F1_MID      = "#2563EB"
F1_LIGHT    = "#DBEAFE"
F1_ENTRY    = "#1E40AF"
F1_ENTRY_L  = "#EFF6FF"
F1_EXIT     = "#1D4ED8"
F1_EXIT_L   = "#BFDBFE"
F1_PROC     = "#3B82F6"
F1_PROC_L   = "#F0F7FF"

# Fig2: verde bosque (estructura/taxonomía)
F2_DARK     = "#14532D"
F2_MID      = "#16A34A"
F2_LIGHT    = "#DCFCE7"
F2_LEVELS   = ["#166534", "#15803D", "#22C55E", "#4ADE80"]
F2_FILLS    = ["#F0FDF4", "#DCFCE7", "#BBF7D0", "#ECFDF5"]

# Fig3: terracota/naranja (análisis conceptual)
F3_DARK     = "#7C2D12"
F3_MID      = "#EA580C"
F3_LIGHT    = "#FED7AA"
F3_STEPS    = ["#9A3412", "#C2410C", "#EA580C", "#FB923C"]
F3_FILLS    = ["#FFF7ED", "#FFF7ED", "#FFF7ED", "#FFEDD5"]

# Fig4: violeta (integración/estructura)
F4_DARK     = "#3B0764"
F4_MID      = "#7C3AED"
F4_LIGHT    = "#EDE9FE"
F4_DIMS     = ["#5B21B6", "#6D28D9", "#7C3AED"]
F4_DIM_F    = ["#F5F3FF", "#EDE9FE", "#F5F3FF"]
F4_RESULT   = "#4C1D95"
F4_RESULT_F = "#EDE9FE"

# Tipografía
plt.rcParams.update({
    "font.family":      "DejaVu Sans",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.spines.left":  False,
    "axes.spines.bottom":False,
})

DPI = 300

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def clear_ax(ax):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("auto")
    ax.axis("off")

def box(ax, x, y, w, h,
        label, sublabel=None,
        fc=WHITE, ec=INK, lw=1.8,
        label_fs=11, sub_fs=8.5,
        label_c=INK, sub_c=MUTED,
        radius=0.012, bold=True,
        shadow=True):
    """Caja redondeada con sombra opcional."""
    if shadow:
        shade = FancyBboxPatch(
            (x + 0.004, y - 0.006), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            fc="#D1D5DB", ec="none", zorder=1)
        ax.add_patch(shade)

    rect = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        fc=fc, ec=ec, lw=lw, zorder=2)
    ax.add_patch(rect)

    cy = y + h / 2
    if sublabel:
        cy_main = y + h * 0.60
        cy_sub  = y + h * 0.28
        weight = "bold" if bold else "normal"
        ax.text(x + w/2, cy_main, label,
                ha="center", va="center",
                fontsize=label_fs, color=label_c,
                fontweight=weight, zorder=3)
        ax.text(x + w/2, cy_sub, sublabel,
                ha="center", va="center",
                fontsize=sub_fs, color=sub_c,
                fontstyle="italic", zorder=3)
    else:
        weight = "bold" if bold else "normal"
        ax.text(x + w/2, cy, label,
                ha="center", va="center",
                fontsize=label_fs, color=label_c,
                fontweight=weight, zorder=3)

def arrow_h(ax, x1, x2, y, color=INK, lw=2.0):
    """Flecha horizontal."""
    ax.annotate("",
        xy=(x2, y), xytext=(x1, y),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            mutation_scale=16),
        zorder=5)

def arrow_v(ax, x, y1, y2, color=INK, lw=2.0):
    """Flecha vertical (de y1 hacia y2)."""
    ax.annotate("",
        xy=(x, y2), xytext=(x, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            mutation_scale=16),
        zorder=5)

def arrow_diag(ax, x1, y1, x2, y2, color=INK, lw=1.8):
    ax.annotate("",
        xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            mutation_scale=14,
            connectionstyle="arc3,rad=0.0"),
        zorder=5)

def fig_header(ax, title, subtitle, accent_color):
    """Cabecera con barra de color, título y subtítulo."""
    # Barra superior
    ax.add_patch(mpatches.Rectangle(
        (0, 0.94), 1.0, 0.06,
        transform=ax.transAxes,
        fc=accent_color, ec="none",
        clip_on=False, zorder=10))
    # Título
    ax.text(0.5, 0.97, title,
            transform=ax.transAxes,
            ha="center", va="center",
            fontsize=14, fontweight="bold",
            color=WHITE, zorder=11)
    # Subtítulo
    ax.text(0.5, 0.915, subtitle,
            transform=ax.transAxes,
            ha="center", va="center",
            fontsize=9, color=MUTED)
    # Línea divisora
    ax.axhline(y=0.895, xmin=0.02, xmax=0.98,
                color=RULE, linewidth=1.0)

def group_bracket(ax, x, y, w, h, label, color, lw=1.5):
    """Corchete superior sobre un grupo de cajas."""
    # Línea horizontal
    ax.plot([x, x+w], [y+h, y+h], color=color, lw=lw, zorder=4)
    # Patillas
    tick = 0.015
    ax.plot([x, x],     [y+h-tick, y+h], color=color, lw=lw, zorder=4)
    ax.plot([x+w, x+w], [y+h-tick, y+h], color=color, lw=lw, zorder=4)
    ax.text(x + w/2, y+h+0.018, label,
            ha="center", va="bottom",
            fontsize=8.5, color=color, fontweight="bold")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 1 — Pipeline de procesamiento
# Identidad: azul académico | Layout horizontal | 3 bloques funcionales
# ══════════════════════════════════════════════════════════════════════════════
def fig1_pipeline():
    fig, ax = plt.subplots(figsize=(16, 7))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    clear_ax(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    fig_header(ax,
               "FIGURA 1. PIPELINE DE PROCESAMIENTO",
               "Secuencia de transformación desde datos crudos hasta el dataset final",
               F1_DARK)

    # ── Layout ──────────────────────────────────────────────────
    bw   = 0.118   # ancho caja
    bh   = 0.200   # alto caja
    by   = 0.38    # y base
    gap  = 0.034   # espacio entre cajas
    x0   = 0.032   # inicio

    # 6 cajas: índices 0=entrada, 1-4=proceso, 5=salida
    steps = [
        ("Carga",       None,          F1_ENTRY_L, F1_ENTRY),
        ("Filtro\nterritorial", None,  F1_PROC_L,  F1_PROC),
        ("Integración", None,          F1_PROC_L,  F1_PROC),
        ("Depuración",  None,          F1_PROC_L,  F1_PROC),
        ("Validación",  None,          F1_PROC_L,  F1_PROC),
        ("Dataset\nfinal", None,       F1_EXIT_L,  F1_EXIT),
    ]

    xs = [x0 + i * (bw + gap) for i in range(len(steps))]

    for i, (label, sub, fc, ec) in enumerate(steps):
        lw = 2.5 if i in (0, 5) else 1.8
        box(ax, xs[i], by, bw, bh,
            label=label, sublabel=sub,
            fc=fc, ec=ec, lw=lw,
            label_fs=10.5, sub_fs=8,
            label_c=ec, radius=0.014,
            shadow=(i in (0, 5)))

        # (números de paso eliminados)

        if i < len(steps) - 1:
            arrow_h(ax,
                    xs[i] + bw + 0.004,
                    xs[i+1] - 0.004,
                    by + bh/2,
                    color=F1_MID, lw=1.8)

    # ── Corchetes de grupo ────────────────────────────────────
    top_y  = by + bh + 0.058
    tick_h = 0.012

    # Entrada
    group_bracket(ax,
                  xs[0] - 0.008, by, bw + 0.016, bh + 0.062,
                  "ENTRADA", F1_ENTRY)

    # Procesamiento (pasos 1–4)
    proc_x  = xs[1] - 0.008
    proc_w  = xs[4] + bw + 0.008 - proc_x
    group_bracket(ax, proc_x, by, proc_w, bh + 0.062,
                  "PROCESAMIENTO", F1_PROC)

    # Resultado
    group_bracket(ax,
                  xs[5] - 0.008, by, bw + 0.016, bh + 0.062,
                  "RESULTADO", F1_EXIT)

    # ── Nota al pie ──────────────────────────────────────────
    ax.text(0.5, 0.06,
            "Fuente: elaboración propia. Cada paso depura y enriquece los registros antes de pasar a la etapa siguiente.",
            ha="center", va="center",
            fontsize=8, color=MUTED, style="italic")

    plt.tight_layout(rect=[0, 0.04, 1, 0.90])
    fig.savefig(OUT / "figura_1_pipeline.png", dpi=DPI, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  ✓ figura_1_pipeline.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 2 — Jerarquía de datos
# Identidad: verde | Layout VERTICAL centrado | Llaves de unión
# ══════════════════════════════════════════════════════════════════════════════
def fig2_jerarquia():
    fig, ax = plt.subplots(figsize=(10, 13))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    clear_ax(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    fig_header(ax,
               "FIGURA 2. JERARQUÍA DE DATOS",
               "Estructura anidada de las unidades de observación",
               F2_DARK)

    # ── Layout vertical centrado ─────────────────────────────
    bw   = 0.54
    bh   = 0.095
    cx   = 0.50            # centro horizontal
    x0   = cx - bw/2

    # y de cada caja (de arriba hacia abajo)
    ys   = [0.74, 0.565, 0.39, 0.155]

    levels = [
        ("VIVIENDA",          "Clave: U_VIVIENDA",   F2_FILLS[0], F2_LEVELS[0], 13),
        ("HOGAR",             "Clave: U_VIVIENDA + P_NROHOG",   F2_FILLS[1], F2_LEVELS[1], 13),
        ("PERSONA",           "Clave: U_VIVIENDA + P_NROHOG + P_NRO_PER", F2_FILLS[2], F2_LEVELS[2], 13),
        ("DATASET INTEGRADO", "Unidad analítica final",          F2_FILLS[3], F2_LEVELS[3], 13),
    ]

    for i, (label, sub, fc, ec, fs) in enumerate(levels):
        accent = (i == 3)
        lw     = 2.8 if accent else 2.0
        box(ax, x0, ys[i], bw, bh,
            label=label, sublabel=sub,
            fc=fc, ec=ec, lw=lw,
            label_fs=fs, sub_fs=8.5,
            label_c=ec, sub_c=MUTED,
            radius=0.012, shadow=accent)

        # Etiqueta de nivel a la izquierda
        nivel = ["Nivel 1", "Nivel 2", "Nivel 3", "Resultado"][i]
        ax.text(x0 - 0.06, ys[i] + bh/2, nivel,
                ha="right", va="center",
                fontsize=8, color=MUTED, style="italic")

        # Indicador de cardinalidad (derecha)
        card = ["1", "1..N", "1..N", "—"][i]
        ax.text(x0 + bw + 0.05, ys[i] + bh/2, card,
                ha="left", va="center",
                fontsize=9, color=ec, fontweight="bold")

    # ── Flechas verticales entre niveles ─────────────────────
    for i in range(3):
        y1 = ys[i]                 # fondo de la caja superior
        y2 = ys[i+1] + bh         # techo de la caja inferior
        color = F2_LEVELS[i+1]

        # Línea punteada de relación
        ax.plot([cx, cx], [y1 - 0.005, y2 + 0.005],
                color=color, lw=1.5,
                linestyle=(0, (4, 3)), zorder=3)
        arrow_v(ax, cx, y1 - 0.005, y2 + 0.005, color=color, lw=1.8)

        # (etiquetas relacionales eliminadas)

    # ── Nota al pie ──────────────────────────────────────────
    ax.text(0.5, 0.07,
            "Fuente: elaboración propia. La integración usa claves jerárquicas para preservar la estructura anidada.",
            ha="center", va="center",
            fontsize=7.5, color=MUTED, style="italic",
            wrap=True)

    plt.tight_layout(rect=[0, 0.04, 1, 0.90])
    fig.savefig(OUT / "figura_2_jerarquia.png", dpi=DPI, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  ✓ figura_2_jerarquia.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 3 — Flujo analítico conceptual
# Identidad: terracota | Layout vertical con 4 etapas conceptuales amplias
# ══════════════════════════════════════════════════════════════════════════════
def fig3_flujo():
    fig, ax = plt.subplots(figsize=(13, 10))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    clear_ax(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    fig_header(ax,
               "FIGURA 3. FLUJO DE TRANSFORMACIÓN ANALÍTICA",
               "De los microdatos crudos a la construcción del dataset analítico",
               F3_DARK)

    # ── Etapas (layout vertical 4 bloques) ──────────────────
    # Cada etapa: caja principal + zona de descripción lateral
    stages = [
        {
            "label":  "MICRODATOS CNPV 2018",
            "sub":    "Fuente primaria · DANE",
            "detail": "Archivos separados por\nvivienda, hogar y persona",
            "ec": F3_STEPS[0], "fc": F3_FILLS[0],
        },
        {
            "label":  "VARIABLES RELEVANTES",
            "sub":    "Selección y filtrado",
            "detail": "Filtro territorial: Cali\nSelección de variables analíticas",
            "ec": F3_STEPS[1], "fc": F3_FILLS[1],
        },
        {
            "label":  "DIMENSIONES TEMÁTICAS",
            "sub":    "Organización conceptual",
            "detail": "Individual · Hogar · Vivienda\nAgrupación por constructo",
            "ec": F3_STEPS[2], "fc": F3_FILLS[2],
        },
        {
            "label":  "DATASET ANALÍTICO",
            "sub":    "Resultado final integrado",
            "detail": "Unidad: persona\nListo para análisis estadístico",
            "ec": F3_STEPS[3], "fc": F3_FILLS[3],
        },
    ]

    bw_main = 0.42
    bh      = 0.110
    x_main  = 0.08
    x_detail= x_main + bw_main + 0.07

    # y posiciones (de arriba abajo)
    ys = [0.740, 0.550, 0.360, 0.135]

    for i, s in enumerate(stages):
        is_last = (i == 3)
        lw = 3.0 if is_last else 2.0

        # Caja principal
        box(ax, x_main, ys[i], bw_main, bh,
            label=s["label"], sublabel=s["sub"],
            fc=s["fc"], ec=s["ec"], lw=lw,
            label_fs=12 if is_last else 11,
            sub_fs=8.5,
            label_c=s["ec"], sub_c=MUTED,
            radius=0.014, shadow=is_last)

        # Caja de detalle (derecha, sin sombra)
        box(ax, x_detail, ys[i] + 0.008, 0.36, bh - 0.016,
            label=s["detail"],
            fc=WHITE, ec=RULE, lw=1.2,
            label_fs=8.5, label_c=MUTED,
            bold=False, radius=0.010, shadow=False)

        # Conector punteado horizontal
        ax.plot([x_main + bw_main, x_detail],
                [ys[i] + bh/2, ys[i] + bh/2],
                color=RULE, lw=1.2, linestyle="dashed", zorder=3)

        # Número de etapa
        ax.text(x_main - 0.04, ys[i] + bh/2,
                str(i+1),
                ha="center", va="center",
                fontsize=16, color=s["ec"],
                fontweight="bold")

        # Flecha vertical hacia la siguiente etapa
        if i < len(stages) - 1:
            arrow_v(ax,
                    x_main + bw_main/2,
                    ys[i] - 0.005,
                    ys[i+1] + bh + 0.005,
                    color=F3_MID, lw=2.2)

    # ── Nota al pie ──────────────────────────────────────────
    ax.text(0.5, 0.055,
            "Fuente: elaboración propia. El flujo refleja las decisiones analíticas, no el procesamiento técnico de archivos.",
            ha="center", va="center",
            fontsize=7.5, color=MUTED, style="italic")

    plt.tight_layout(rect=[0, 0.04, 1, 0.90])
    fig.savefig(OUT / "figura_3_flujo_analitico.png", dpi=DPI, bbox_inches="tight",
                facecolor=BG)
    plt.close()
    print("  ✓ figura_3_flujo_analitico.png")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 4 — Estructura conceptual del dataset
# Identidad: violeta | Tres dimensiones convergiendo en dataset central
# ══════════════════════════════════════════════════════════════════════════════
def fig4_estructura():
    fig, ax = plt.subplots(figsize=(15, 10))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    clear_ax(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    fig_header(ax,
               "FIGURA 4. ESTRUCTURA CONCEPTUAL DEL DATASET FINAL",
               "Integración de tres dimensiones en un único dataset socioeconómico",
               F4_DARK)

    # ── Dataset central (abajo, grande) ─────────────────────
    res_bw, res_bh = 0.54, 0.160
    res_cx = 0.50
    res_y  = 0.105
    res_x  = res_cx - res_bw/2

    box(ax, res_x, res_y, res_bw, res_bh,
        label="DATASET SOCIOECONÓMICO",
        sublabel="Unidad de análisis: persona",
        fc=F4_LIGHT, ec=F4_RESULT, lw=3.2,
        label_fs=15, sub_fs=9,
        label_c=F4_RESULT, sub_c=MUTED,
        radius=0.016, shadow=True)

    # ── Tres dimensiones (arriba) ────────────────────────────
    dims = [
        {
            "label":    "DIMENSIÓN\nINDIVIDUAL",
            "sub":      "Variables de persona",
            "examples": "Edad · Sexo · Educación\nOcupación · Ingresos",
            "cx": 0.18,
        },
        {
            "label":    "DIMENSIÓN\nHOGAR",
            "sub":      "Variables del hogar",
            "examples": "Tamaño · Ingresos\nJefatura · Tipo",
            "cx": 0.50,
        },
        {
            "label":    "DIMENSIÓN\nVIVIENDA",
            "sub":      "Variables de vivienda",
            "examples": "Tipo · Tenencia\nAcceso a servicios",
            "cx": 0.82,
        },
    ]

    dim_bw = 0.22
    dim_bh = 0.130
    ex_bw  = 0.20
    ex_bh  = 0.095
    dim_y  = 0.590    # y base de las dimensiones
    ex_y   = 0.420    # y base de los ejemplos

    for i, d in enumerate(dims):
        dx = d["cx"] - dim_bw/2

        # Caja dimensión
        box(ax, dx, dim_y, dim_bw, dim_bh,
            label=d["label"], sublabel=d["sub"],
            fc=F4_DIM_F[i], ec=F4_DIMS[i], lw=2.2,
            label_fs=10.5, sub_fs=8,
            label_c=F4_DIMS[i], sub_c=MUTED,
            radius=0.013, shadow=False)

        # Caja ejemplos (debajo de la dimensión)
        ex_x = d["cx"] - ex_bw/2
        box(ax, ex_x, ex_y, ex_bw, ex_bh,
            label=d["examples"],
            fc=WHITE, ec=RULE, lw=1.0,
            label_fs=8, label_c=MUTED,
            bold=False, radius=0.010, shadow=False)

        # Conector dimensión → ejemplo
        ax.plot([d["cx"], d["cx"]],
                [dim_y - 0.004, ex_y + ex_bh + 0.004],
                color=RULE, lw=1.2, linestyle="dotted", zorder=3)

        # Flecha: ejemplo → dataset
        ax.annotate("",
            xy=(res_cx, res_y + res_bh + 0.003),
            xytext=(d["cx"], ex_y - 0.005),
            arrowprops=dict(
                arrowstyle="-|>",
                color=F4_DIMS[i],
                lw=1.8,
                mutation_scale=14,
                connectionstyle="arc3,rad=0.0"),
            zorder=5)

        # Etiqueta de variable count (opcional, visual)
        ax.text(d["cx"], dim_y + dim_bh + 0.025,
                ["N₁ variables", "N₂ variables", "N₃ variables"][i],
                ha="center", va="bottom",
                fontsize=7.5, color=F4_DIMS[i])

    # ── Línea de integración: franja horizontal sutil ─────────
    fuse_y = res_y + res_bh + 0.008
    ax.axhline(fuse_y, xmin=0.04, xmax=0.96,
               color=F4_MID, lw=0.8, alpha=0.35, linestyle="solid")
    ax.text(0.975, fuse_y + 0.005, "INTEGRACIÓN",
            ha="right", va="bottom",
            fontsize=7, color=F4_MID, alpha=0.7,
            fontweight="bold", style="italic")

    # ── Nota al pie ──────────────────────────────────────────
    ax.text(0.5, 0.040,
            "Fuente: elaboración propia. Las variables de cada dimensión se vinculan a nivel de persona mediante claves jerárquicas.",
            ha="center", va="center",
            fontsize=7.5, color=MUTED, style="italic")

    plt.tight_layout(rect=[0, 0.03, 1, 0.90])
    fig.savefig(OUT / "figura_4_estructura_dataset.png", dpi=DPI,
                bbox_inches="tight", facecolor=BG)
    plt.close()
    print("  ✓ figura_4_estructura_dataset.png")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generando figuras para tesis…\n")
    fig1_pipeline()
    fig2_jerarquia()
    fig3_flujo()
    fig4_estructura()
    print(f"\n✓ Listo. Archivos en: {OUT.resolve()}")