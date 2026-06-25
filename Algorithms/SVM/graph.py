"""
graph.py — helper module for svm_scikit.ipynb
Provides sample data and matplotlib drawing utilities for SVM visualisation.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Sample 2D dataset: two linearly separable clusters
points = [
    [1, 2], [2, 3], [1, 4], [3, 2],   # class 0
    [5, 6], [6, 5], [7, 6], [6, 7],   # class 1
]

labels = [0, 0, 0, 0, 1, 1, 1, 1]


def draw_points(pts, lbls):
    """Scatter-plot pts coloured by lbls (0 = blue, 1 = red)."""
    pts = np.array(pts)
    lbls = np.array(lbls)
    colors = np.where(lbls == 0, "steelblue", "tomato")
    plt.scatter(pts[:, 0], pts[:, 1], c=colors, edgecolors="k", s=60, zorder=3)
    patch0 = mpatches.Patch(color="steelblue", label="Class 0")
    patch1 = mpatches.Patch(color="tomato",    label="Class 1")
    plt.legend(handles=[patch0, patch1])


def draw_margin(classifier):
    """
    Draw the SVM decision boundary and ±1 margin lines for a fitted
    sklearn SVC with a linear kernel.

    Falls back to a simple decision-function contour for non-linear kernels.
    """
    ax = plt.gca()
    xlim = ax.get_xlim() if ax.get_xlim() != (0.0, 1.0) else (0, 10)
    ylim = ax.get_ylim() if ax.get_ylim() != (0.0, 1.0) else (0, 10)

    # Build a grid and evaluate the decision function
    xx = np.linspace(xlim[0], xlim[1], 200)
    yy = np.linspace(ylim[0], ylim[1], 200)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = classifier.decision_function(xy).reshape(XX.shape)

    # Decision boundary (0) and margin lines (±1) for linear SVM;
    # for other kernels only the boundary is drawn.
    if hasattr(classifier, "coef_"):
        levels = [-1, 0, 1]
        linestyles = ["--", "-", "--"]
        colors_list = ["grey", "black", "grey"]
    else:
        levels = [0]
        linestyles = ["-"]
        colors_list = ["black"]

    ax.contour(
        XX, YY, Z,
        levels=levels,
        linestyles=linestyles,
        colors=colors_list,
        linewidths=[1, 2, 1][:len(levels)],
    )
