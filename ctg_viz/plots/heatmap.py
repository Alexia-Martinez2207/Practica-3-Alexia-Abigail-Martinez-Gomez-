import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def correlation_heatmap(df: pd.DataFrame, method: str = "pearson"):
    """
    Heatmap with selectable correlation method.

    Returns
    -------
    None
    """
    corr = df.corr(method=method)

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title(f"Matriz de correlación ({method})")
    plt.show()
