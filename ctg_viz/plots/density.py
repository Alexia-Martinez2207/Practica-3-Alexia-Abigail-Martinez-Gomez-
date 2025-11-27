import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def density_plot(df: pd.DataFrame, column: str, group: str = None):
    """
    Density plot with multiple classes.

    Returns
    -------
    None
    """
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=df, x=column, hue=group, fill=True, alpha=0.4)
    plt.title(f"Densidad de {column}")
    plt.grid(True, alpha=0.3)
    plt.show()
