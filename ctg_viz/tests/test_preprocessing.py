import pandas as pd
from ctg_viz.preprocessing import remove_high_nulls, impute_missing_values, detect_outliers_iqr

def test_remove_high_nulls():
    df = pd.DataFrame({
        "A": [1, None, None],
        "B": [1, 2, 3]
    })
    
    result = remove_high_nulls(df, threshold=0.5)

    # A debe removerse (66% nulos), B quedarse
    assert "A" not in result.columns
    assert "B" in result.columns

def test_impute_missing_values():
    df = pd.DataFrame({
        "num": [1, None, 3],
        "cat": ["a", None, "b"]
    })

    result = impute_missing_values(df)

    assert result["num"].isnull().sum() == 0
    assert result["cat"].isnull().sum() == 0

def test_detect_outliers_iqr():
    df = pd.DataFrame({"x": [1, 2, 3, 100]})

    outliers = detect_outliers_iqr(df["x"])

    assert len(outliers) == 1
    assert outliers.iloc[0] == 100
