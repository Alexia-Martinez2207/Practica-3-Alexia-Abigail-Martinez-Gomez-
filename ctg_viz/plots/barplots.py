import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def horizontal_barplot(df: pd.DataFrame, column: str):
    """
    Horizontal barplot sorted descending.

    Returns
    -------
    None
    """
    counts = df[column].value_counts().sort_values(ascending=True)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=counts, y=counts.index)
    plt.title(f"Barras horizontales de {column}")
    plt.xlabel("Frecuencia")
    plt.ylabel(column)
    plt.grid(True, alpha=0.3)
    plt.show()
