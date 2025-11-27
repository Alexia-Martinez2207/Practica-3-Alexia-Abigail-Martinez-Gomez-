import pandas as pd
from ctg_viz.plots.histograms import plot_histogram
from ctg_viz.plots.boxplots import boxplot_by_class
from ctg_viz.plots.barplots import horizontal_barplot

def test_plot_histogram_runs():
    df = pd.DataFrame({"x": [1, 2, 3, 4]})
    fig = plot_histogram(df, "x")
    assert fig is not None

def test_boxplot_by_class_runs():
    df = pd.DataFrame({
        "value": [1, 2, 3, 4],
        "class": ["A", "A", "B", "B"]
    })
    fig = boxplot_by_class(df, "value", "class")
    assert fig is not None

def test_horizontal_barplot_runs():
    df = pd.DataFrame({"cat": ["a", "b", "b", "c", "c", "c"]})
    fig = horizontal_barplot(df, "cat")
    assert fig is not None
