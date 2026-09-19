"""Generate matplotlib/seaborn figures for the OR exam notes.

Run with: pdfenv/Scripts/python.exe Notes/figures/make_graphs.py
(from the project root). Outputs PNGs into Notes/figures/.
All plotted numbers come from the worked examples in Notes/Modules 1, 4, 5.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Polygon
from pathlib import Path

FIG = Path(__file__).parent
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.size": 10, "figure.dpi": 150})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(FIG / name, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


def g_lp_unique():
    """Lec 3: Max z=5x1+3x2 s.t. x1+x2<=5, 3x1+8x2<=24. Opt C(5,0), z*=25."""
    fig, ax = plt.subplots(figsize=(6, 4.6))
    x = np.linspace(0, 8, 400)
    ax.plot(x, 5 - x, label=r"$x_1+x_2=5$")
    ax.plot(x, (24 - 3 * x) / 8, label=r"$3x_1+8x_2=24$")
    region = Polygon([(0, 0), (0, 3), (3.2, 1.8), (5, 0)],
                     closed=True, color="skyblue", alpha=0.5, label="Feasible region OABC")
    ax.add_patch(region)
    for z, st in [(10, "--"), (25, "-")]:
        ax.plot(x, (z - 5 * x) / 3, "k", ls=st, lw=1.2 if z == 25 else 0.9, alpha=0.9)
    ax.text(6.2, 1.4, "z=10", rotation=-55)
    ax.text(5.4, 2.6, "z=25 (opt)", rotation=-55, fontweight="bold")
    for (px, py), nm, z in [((0, 0), "O", 0), ((0, 3), "A", 9),
                            ((3.2, 1.8), "B", 21.4), ((5, 0), "C", 25)]:
        ax.plot(px, py, "ko")
        ax.annotate(f"{nm}({px},{py})\nz={z}", (px, py), textcoords="offset points",
                    xytext=(8, 6 if py < 2 else -18))
    ax.plot(5, 0, "r*", ms=14, label="Optimum C, z*=25")
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 8.5)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$")
    ax.set_title("Unique optimum: max $z=5x_1+3x_2$ (Lec 3)")
    ax.legend(loc="upper right", fontsize=8)
    save(fig, "g_lp_unique.png")


def g_lp_multiple():
    """Lec 3: Max z=3x1+8x2, same region. Whole segment AB optimal, z=24."""
    fig, ax = plt.subplots(figsize=(6, 4.6))
    x = np.linspace(0, 8, 400)
    ax.plot(x, 5 - x, label=r"$x_1+x_2=5$")
    ax.plot(x, (24 - 3 * x) / 8, label=r"$3x_1+8x_2=24$")
    ax.add_patch(Polygon([(0, 0), (0, 3), (3.2, 1.8), (5, 0)],
                          closed=True, color="skyblue", alpha=0.5, label="Feasible region"))
    ax.plot([0, 3.2], [3, 1.8], "r-", lw=4, alpha=0.8, label="Optimal segment AB (z=24)")
    ax.plot(x, (24 - 3 * x) / 8, "r--", lw=1, alpha=0.6)
    ax.text(4.5, 3.4, "iso-line z=24 overlaps AB", color="darkred")
    for (px, py), nm in [((0, 3), "A"), ((3.2, 1.8), "B")]:
        ax.plot(px, py, "ro", ms=8)
        ax.annotate(f"{nm}", (px, py), textcoords="offset points", xytext=(6, 4),
                    fontweight="bold")
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 8.5)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$")
    ax.set_title("Multiple optima: max $z=3x_1+8x_2$ (Lec 3)")
    ax.legend(loc="upper right", fontsize=8)
    save(fig, "g_lp_multiple.png")


def g_lp_unbounded():
    """Lec 3: Max z=3x1+8x2 s.t. 2x1-x2>=0, x2<=4. Open to the right."""
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.plot([0, 9], [0, 18], label=r"$2x_1-x_2=0$  ($x_2=2x_1$)")
    ax.axhline(4, color="C1", label=r"$x_2=4$")
    ax.add_patch(Polygon([(0, 0), (2, 4), (9, 4), (9, 0)], closed=True,
                          color="skyblue", alpha=0.5, label="Feasible (open right)"))
    ax.plot([9, 9], [0, 4], "k--", lw=1)
    ax.annotate("extends to infinity", (9, 2), xytext=(6.2, 5.6),
                arrowprops=dict(arrowstyle="->"), fontweight="bold")
    ax.plot(0, 0, "ko"); ax.text(0.15, 0.25, "O")
    ax.plot(2, 4, "ko"); ax.text(2.1, 4.15, "A(2,4)")
    ax.quiver(4, 2, 3, 8, scale=25, color="darkred", width=0.008)
    ax.text(4.6, 3.1, "z grows unbounded", color="darkred", fontweight="bold")
    ax.set_xlim(0, 9.5); ax.set_ylim(0, 8)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$")
    ax.set_title("Unbounded: max $z=3x_1+8x_2$ (Lec 3)")
    ax.legend(loc="upper left", fontsize=8)
    save(fig, "g_lp_unbounded.png")


def g_lp_infeasible():
    """Lec 3: x1+x2<=5 vs x1+x2>=6. Parallel strips, no overlap."""
    fig, ax = plt.subplots(figsize=(6, 4.6))
    x = np.linspace(0, 8, 400)
    ax.fill_between(x, 0, np.clip(5 - x, 0, None), color="skyblue",
                    alpha=0.5, hatch="///", edgecolor="C0", label=r"$x_1+x_2 \leq 5$")
    ax.fill_between(x, np.clip(6 - x, 0, None), 9, color="salmon",
                    alpha=0.5, hatch="\\\\\\", edgecolor="C3", label=r"$x_1+x_2 \geq 6$")
    ax.plot(x, 5 - x, "C0", lw=1.5)
    ax.plot(x, 6 - x, "C3", lw=1.5)
    ax.text(1.2, 5.6, "strip 1", color="C0", fontweight="bold")
    ax.text(5.6, 1.6, "strip 2", color="C3", fontweight="bold")
    ax.text(2.5, 4.0, "NO overlap: infeasible", fontsize=12,
            color="darkred", fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="darkred"))
    ax.set_xlim(0, 8.5); ax.set_ylim(0, 8.5)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$")
    ax.set_title("Infeasible: contradictory constraints (Lec 3)")
    ax.legend(loc="upper right", fontsize=8)
    save(fig, "g_lp_infeasible.png")


def g_convex_nonconvex():
    """Lec 4: convex set (chord stays inside) vs non-convex L-shape (chord exits)."""
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.8))
    hexagon = np.array([[0.5, 0.2], [2.2, 0.2], [3.0, 1.2], [2.2, 2.4], [0.8, 2.4], [0.1, 1.2]])
    ax = axes[0]
    ax.add_patch(Polygon(hexagon, closed=True, color="skyblue", alpha=0.6, edgecolor="C0", lw=1.5))
    p, q = hexagon[1], hexagon[4]
    ax.plot([p[0], q[0]], [p[1], q[1]], "g-", lw=2)
    ax.plot([p[0], q[0]], [p[1], q[1]], "go")
    ax.set_title("Convex: chord PQ inside")
    ax.set_aspect("equal"); ax.axis("off")
    ax = axes[1]
    ell = np.array([[0, 0], [3, 0], [3, 1], [1, 1], [1, 3], [0, 3]])
    ax.add_patch(Polygon(ell, closed=True, color="salmon", alpha=0.6, edgecolor="C3", lw=1.5))
    p, q = np.array([2.5, 0.5]), np.array([0.5, 2.5])
    mid = (p + q) / 2
    ax.plot([p[0], q[0]], [p[1], q[1]], "r--", lw=2)
    ax.plot([p[0], q[0]], [p[1], q[1]], "ro")
    ax.plot(mid[0], mid[1], "rx", ms=12, mew=2)
    ax.text(mid[0] + 0.1, mid[1] + 0.1, "outside!", color="darkred", fontweight="bold")
    ax.set_title("Non-convex (L-shape): chord exits")
    ax.set_aspect("equal"); ax.axis("off")
    fig.suptitle("Convex vs non-convex sets (Lec 4)")
    save(fig, "g_convex_nonconvex.png")


def g_transport_costs():
    """Lec 28: IBFS costs NW=1015, Least-cost=814, VAM=779, MODI optimum=547."""
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    methods = ["NW-corner", "Least-cost", "VAM", "Optimum\n(MODI)"]
    costs = [1015, 814, 779, 547]
    sns.barplot(x=methods, y=costs, hue=methods, palette="Blues_d", legend=False, ax=ax)
    for i, c in enumerate(costs):
        ax.text(i, c + 18, str(c), ha="center", fontweight="bold")
    ax.set_ylim(0, 1150)
    ax.set_ylabel("Cost (Rs)")
    ax.set_title("Transportation: IBFS methods vs optimum (Lec 28)")
    save(fig, "g_transport_costs.png")


def g_game_2x4():
    """Lec 38: 2x4 game lines E_k(x), lower envelope, maximin at x*=15/16, V=245/16."""
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    lines = {"E1 (col 1)": lambda t: 19 * t,
             "E2 (col 2)": lambda t: 20 - 5 * t,
             "E3 (col 3)": lambda t: 15 + 2 * t,
             "E4 (col 4)": lambda t: 5 + 11 * t}
    t = np.linspace(0, 1, 501)
    vals = np.array([[f(ti) for ti in t] for f in lines.values()])
    for (nm, _), v in zip(lines.items(), vals):
        ax.plot(t, v, lw=1.2, label=nm)
    env = vals.min(axis=0)
    ax.plot(t, env, "k-", lw=3, label="Lower envelope")
    xs, V = 15 / 16, 245 / 16
    ax.plot(xs, V, "r*", ms=15, label=f"Maximin x*={xs:.4f}, V={V:.4f}")
    ax.annotate(f"peak C: intersection of E2,E4\nx*=15/16, V=245/16",
                (xs, V), xytext=(0.30, 17.5),
                arrowprops=dict(arrowstyle="->", color="darkred"), color="darkred")
    ax.set_xlim(0, 1); ax.set_xlabel("x = P(A1)")
    ax.set_ylabel("Expected payoff E")
    ax.set_title("2x4 game: lower envelope + maximin (Lec 38)")
    ax.legend(loc="lower left", fontsize=8)
    save(fig, "g_game_2x4.png")


if __name__ == "__main__":
    g_lp_unique()
    g_lp_multiple()
    g_lp_unbounded()
    g_lp_infeasible()
    g_convex_nonconvex()
    g_transport_costs()
    g_game_2x4()
    print("ALL GRAPHS DONE")
