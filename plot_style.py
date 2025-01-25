# plot_style.py
import matplotlib.pyplot as plt
from cycler import cycler

def set_plot_style():
    """Set a consistent style guide for Matplotlib plots."""
    # Set the overall style
    plt.style.use("seaborn-v0_8-whitegrid")  # Base style

    # Custom color cycle (choose your preferred colors)
    #colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    colors = ["#000", "#000", "#000", "#000", "#888", "#888", "#888", "#888"]
    linestyles = ["-", "--", "-.", ":", "-", "--", "-.", ":"]  # Line style order
    plt.rcParams["axes.prop_cycle"] = cycler(color=colors, linestyle=linestyles)

    # Font settings
    plt.rcParams["font.size"] = 12
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica", "DejaVu Sans"]

    # Axes settings
    plt.rcParams["axes.titlesize"] = 13  # Title font size
    plt.rcParams["axes.titleweight"] = "bold"  # Title font size
    plt.rcParams["axes.labelsize"] = 12  # Axis label font size
    plt.rcParams["axes.grid"] = True  # Show grid
    plt.rcParams["grid.alpha"] = 0.5  # Grid transparency
    plt.rcParams["axes.spines.top"] = False  # Hide top spine
    plt.rcParams["axes.spines.right"] = False  # Hide right spine

    # Tick settings
    plt.rcParams["xtick.labelsize"] = 10  # X-tick label size
    plt.rcParams["ytick.labelsize"] = 10  # Y-tick label size
    plt.rcParams["xtick.direction"] = "out"  # Tick direction
    plt.rcParams["ytick.direction"] = "out"

    # Line and marker settings
    plt.rcParams["lines.linewidth"] = 1  # Line width
    plt.rcParams["lines.markersize"] = 6  # Marker size

    # Legend settings
    plt.rcParams["legend.fontsize"] = 8
    plt.rcParams["legend.frameon"] = False  # No frame around the legend
    plt.rcParams["legend.loc"] = "lower left"  # Place legend at the best location



    # Figure settings
    plt.rcParams["figure.figsize"] = (8, 5)  # Default figure size
    plt.rcParams["figure.dpi"] = 100  # Figure resolution

# Example usage
if __name__ == "__main__":
    set_plot_style()

    # Example plot
    import numpy as np

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label="Sine Wave")
    plt.plot(x, y2, label="Cosine Wave")
    plt.title("Example Plot with Custom Style")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()