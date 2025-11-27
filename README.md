# Practica-3-Alexia-Abigail-Martinez-Gomez-
El presente repositorio es un análisis de una base de datos de cardiología con el tratamiento indicado.
## Objetivo

Profundizar en el análisis exploratorio de datos mediante la creación de una **librería personalizada de visualización** con funciones reutilizables, aplicando buenas prácticas de desarrollo y análisis estadístico.

---

## Dataset

- **Archivo:** `CTG.csv` – Cardiotocography Data Set (Kaggle)  
- **Descripción:** Conjunto de datos de registros cardiotocográficos con diversas características diagnósticas y etiquetas de clasificación.

---

## Preprocesamiento de Datos

- Se eliminaron columnas con más del **20% de valores nulos**.  
- Los valores faltantes restantes se imputaron:  
  - **Numéricos:** media y mediana  
  - **Categóricos:** moda  
- Detección y tratamiento de **outliers** pendiente (IQR o z-score) según el reto de la práctica.  

---

## Análisis de Datos

Se creó la función:

check_data_completeness_numer(df: pd.DataFrame) -> pd.DataFrame
Que realiza:
* Conteo de valores nulos
* Porcentaje de completitud
* Tipo de dato
* Estadísticos de dispersión (min, max, std, var, IQR)
* Clasificación de columnas en:
* Continuas: >10 valores únicos
* Discretas: ≤10 valores únicos
  
Ejemplo de uso:

resumen = check_data_completeness_numer(df)
print(resumen)

Visualizaciones
Se implementaron varias funciones de visualización personalizadas:

1. Histograma
Función estática con seaborn:

plot_histogram(df, column="LB", kde=True)

plot_histogram(df, column="LB", group="NSP")

plot_histogram(df, "AC", bins=50)

Permite agrupar por categoría (group) y mostrar KDE (línea de densidad).

Configuración de bins y tamaño de figura.

2. Histograma Interactivo

Función con Plotly para exploración dinámica:

plot_histogram_interactive(df, "LB", group="NSP")
Permite zoom, hover y exploración de los datos de manera interactiva.

3. Boxplots por clase

Función con Plotly que genera subplots por clase objetivo:

boxplot_by_class(df, numeric_col="LB", class_col="NSP")

Cada clase se muestra en un subplot separado.
Incluye media en cada boxplot.

El código puede organizarse como un módulo ctg_viz/ con submódulos:

ctg_viz/

├── __init__.py

├── preprocessing.py

├── categorization.py

├── plots/

│   ├── histograms.py

│   ├── boxplots.py

│   ├── barplots.py

│   ├── density.py

│   └── heatmap.py

├── utils.py

Ejemplo de uso de las funciones directamente:

from ctg_viz.preprocessing import check_data_completeness_numer

from ctg_viz.plots.histograms import plot_histogram

from ctg_viz.plots.boxplots import boxplot_by_class

resumen = check_data_completeness_numer(df)

plot_histogram(df, column="LB", kde=True)

boxplot_by_class(df, numeric_col="LB", class_col="NSP")
