# Practica-3-Alexia-Abigail-Martinez-Gomez-
El presente repositorio es un análisis de una base de datos de cardiología con el tratamiento indicado.
## Objetivo

Profundizar en el análisis exploratorio de datos mediante la creación de una **librería personalizada de visualización** con funciones reutilizables, aplicando buenas prácticas de desarrollo y análisis estadístico.

---

## Dataset

- **Archivo:** `CTG.csv` – Cardiotocography Data Set (Kaggle)  
- **Descripción:** Conjunto de datos de registros cardiotocográficos con diversas características diagnósticas y etiquetas de clasificación.

---

## Requisitos de la Práctica

### 1. Preprocesamiento
- Eliminar columnas con más del **20% de valores nulos**.  
- Imputar valores faltantes restantes usando:  
  - Media / mediana para numéricos  
  - Moda para categóricos  
- Detectar y tratar **valores atípicos (outliers)** con IQR o z-score.

### 2. Análisis de Datos
- Crear función `check_data_completeness_nombrecompleto(df)` que retorne:  
  - Conteo de nulos  
  - Porcentaje de completitud  
  - Tipo de dato  
  - Estadísticos de dispersión  
- Clasificar automáticamente columnas en:  
  - **Continuas:** más de 10 valores únicos y tipo numérico  
  - **Discretas:** menos de 10 valores únicos

### 3. Visualizaciones
- Crear gráficos con funciones personalizadas y opcionalmente interactivas:  
  - **Histogramas:** línea de densidad + KDE + customizable por grupo  
  - **Boxplots:** subgráficos por clase objetivo  
  - **Barras horizontales:** ordenadas por frecuencia descendente  
  - **Líneas:** simular serie temporal  
  - **Dot plots:** comparación entre 2 grupos (overlay)  
  - **Densidad:** múltiples clases con colores distintos  
  - **Violín:** overlay con swarmplot  
  - **Heatmap:** correlación + anotaciones y selección de método (`pearson`, `spearman`)

### 4. Librería Python
- Crear módulo `ctg_viz/` con la siguiente estructura:

ctg_viz/
├── init.py
├── preprocessing.py
├── categorization.py
├── plots/
│ ├── histograms.py
│ ├── boxplots.py
│ ├── barplots.py
│ ├── density.py
│ └── heatmap.py
├── utils.py

- Todo el código debe tener:  
  - **Tipado estático**: `def func(x: pd.DataFrame) -> pd.DataFrame`  
  - **Docstrings** (estilo Google o NumPy)  
  - **Pruebas básicas** con pytest

### 5. Validación y Reporte
- Crear **pruebas unitarias** para al menos 4 funciones clave  
- Generar **Jupyter Notebook de ejemplo** con uso de cada función  
- Exportar **reporte en PDF** con:  
  - Descripción de funciones  
  - Visualizaciones generadas  
  - Recomendaciones analíticas breves

---

Ejemplo de uso de la librería:
from ctg_viz.preprocessing import imputar_valores
from ctg_viz.plots.histograms import plot_histogram

# Cargar dataset
import pandas as pd
df = pd.read_csv("CTG.csv")

# Preprocesar datos
df = imputar_valores(df)

# Visualizar
plot_histogram(df, columna="FHR")


Para más ejemplos, consultar el Notebook de demostración incluido.
