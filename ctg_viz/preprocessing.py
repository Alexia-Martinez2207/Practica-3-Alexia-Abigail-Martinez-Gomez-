import pandas as pd
import numpy as np
from typing import Tuple


def remove_high_null_columns(df: pd.DataFrame, threshold: float = 0.2) -> pd.DataFrame:
    """
    Remove columns with more than a % threshold of null values.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    threshold : float
        Maximum percentage of nulls allowed.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe.
    """
    null_ratio = df.isnull().mean()
    return df.loc[:, null_ratio < threshold]


def impute_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Impute missing values:
    - Mean/median for numeric
    - Mode for categorical

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)

    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Detect outliers using the IQR rule.

    Returns
    -------
    pd.DataFrame
        Rows marked as outliers.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    mask = (df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)
    return df[mask]


def treat_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Cap outliers using IQR fences.

    Returns
    -------
    pd.DataFrame
    """
    df = df.copy()
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[column] = np.clip(df[column], lower, upper)

    return df
