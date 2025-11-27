import pandas as pd
from typing import Dict


def check_data_completeness(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze nulls, data type, dispersion stats and classify as continuous/discrete.

    Returns
    -------
    pd.DataFrame
    """
    results = []

    for col in df.columns:
        series = df[col]
        dtype = series.dtype
        n_nulls = series.isnull().sum()
        completeness = 1 - (n_nulls / len(series))

        metrics = {
            "min": series.min() if pd.api.types.is_numeric_dtype(series) else None,
            "max": series.max() if pd.api.types.is_numeric_dtype(series) else None,
            "std": series.std() if pd.api.types.is_numeric_dtype(series) else None,
            "var": series.var() if pd.api.types.is_numeric_dtype(series) else None,
            "iqr": (series.quantile(0.75) - series.quantile(0.25))
            if pd.api.types.is_numeric_dtype(series) else None
        }

        n_unique = series.nunique()
        classification = (
            "Continua" if pd.api.types.is_numeric_dtype(series) and n_unique > 10
            else "Discreta"
        )

        results.append({
            "columna": col,
            "tipo": str(dtype),
            "n_nulos": n_nulls,
            "completitud": completeness,
            "min": metrics["min"],
            "max": metrics["max"],
            "std": metrics["std"],
            "var": metrics["var"],
            "iqr": metrics["iqr"],
            "clasificación": classification
        })

    return pd.DataFrame(results)
