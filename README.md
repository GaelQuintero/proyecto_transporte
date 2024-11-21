# Proyecto de Análisis de Transporte 🚍

Este proyecto utiliza datos ficticios generados con [Mockaroo](https://mockaroo.com) para realizar un análisis de transporte aplicando **algoritmos de aprendizaje no supervisado** con Python y scikit-learn. 

El objetivo es identificar patrones en el comportamiento de los usuarios, las rutas más utilizadas y los costos asociados a los diferentes medios de transporte.

---

## 📂 Estructura del Proyecto

```plaintext
proyecto_transporte/
│
├── data/
│   ├── raw/             # Datos originales generados con Mockaroo
│   └── processed/       # Datos procesados (listos para análisis)
│
├── notebooks/           # Notebooks para experimentación inicial
│
├── src/                 # Código fuente del proyecto
│   ├── data_loading.py  # Funciones para cargar y unir datos
│   ├── preprocessing.py # Limpieza y transformación de datos
│   ├── clustering.py    # Implementación de algoritmos
│   ├── visualization.py # Generación de gráficos
│   └── utils.py         # Funciones auxiliares
│
├── outputs/             # Resultados generados (gráficos, clusters, etc.)
├── tests/               # Pruebas unitarias
├── main.py              # Flujo principal del proyecto
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo
