**Estimated Surgery Time for Patient**
Aplicación en Python para estimar la duración de una intervención quirúrgica por paciente a partir de variables preoperatorias. El proyecto incluye el modelo entrenado, un notebook con el proceso de modelado y una app sencilla para realizar predicciones con el modelo. 
GitHub

**Tecnologías principales:** Python, scikit-learn (modelo serializado con joblib), pandas/numpy (preprocesado), y una app web ligera para inferencia.

**Funcionalidades**
- Predicción de tiempo quirúrgico: dado un conjunto de características del paciente / intervención, devuelve una estimación de la duración esperada.
- Modelo preentrenado: se distribuye como mejor_modelo_1.joblib para usarlo directamente sin volver a entrenar. 
- Notebook de modelado: product_modelo.ipynb documenta el proceso de preparación de datos, entrenamiento y evaluación del modelo. 

El notebook product_modelo.ipynb contiene:
- Carga y limpieza de datos (LOD.csv).
- Selección/ingeniería de variables.
- Entrenamiento del/los modelo(s) y comparación.
- Serialización del mejor modelo a mejor_modelo_1.joblib.
- Métricas de rendimiento (p. ej., MAE/MSE/R²) y validación.

