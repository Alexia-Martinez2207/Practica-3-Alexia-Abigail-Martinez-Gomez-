import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Optional


def histogram(df: pd.DataFrame, column: str, group: Optional[str] = None,
              bins: int = 30, kde: bool = True):
    """
    Plot histogram with optional KDE and grouping.

    Returns
    -------
    None
    """
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x=column,
        hue=group,
        bins=bins,
        kde=kde,
        stat="density",
        common_norm=False
    )

    plt.title(f"Histograma de {column}")
    plt.grid(True, alpha=0.3)
    plt.show()
