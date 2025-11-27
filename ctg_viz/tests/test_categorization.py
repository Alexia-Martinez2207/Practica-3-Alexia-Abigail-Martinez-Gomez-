import pandas as pd
from ctg_viz.categorization import check_data_completeness

def test_check_data_completeness():
    df = pd.DataFrame({
        "num": [1, 2, 3],
        "disc": [1, 1, 2]
    })

    result = check_data_completeness(df)

    # Debe tener ambas columnas
    assert "num" in result["columna"].values
    assert "disc" in result["columna"].values

    # Debe tener columnas calculadas
    assert "porcentaje_completitud" in result.columns
    assert "clasificacion" in result.columns
