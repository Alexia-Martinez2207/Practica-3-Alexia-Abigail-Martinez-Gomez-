import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def boxplot_by_class(df: pd.DataFrame, numeric_col: str, class_col: str):
    """
    Create multiple boxplots separated by class.

    Returns
    -------
    None
    """
    classes = df[class_col].unique()
    fig = make_subplots(rows=1, cols=len(classes),
                        subplot_titles=[f"{class_col}: {c}" for c in classes])

    for i, cls in enumerate(classes, start=1):
        subset = df[df[class_col] == cls]
        fig.add_trace(
            go.Box(y=subset[numeric_col], boxmean=True),
            row=1, col=i
        )

    fig.update_layout(height=500, width=300 * len(classes))
    fig.show()
