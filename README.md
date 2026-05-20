# Simulación: Álbum de Estampas (Coleccionista)

Este repositorio contiene una simulación en Python del problema del "álbum de estampas" (coupon collector) implementada en `index.py`.

**Descripción**
- El programa simula la compra de sobres que contienen varias estampas hasta completar un álbum de tamaño N.
- Realiza R simulaciones y devuelve estadísticas (media, desviación estándar, probabilidad de necesitar más de X sobres), además de comparar con el valor teórico del coleccionista.
- Genera dos gráficas: un histograma del número de sobres necesarios y la probabilidad de completar el álbum al comprar M sobres.

**Requisitos**
- Python 3.8+
- Paquetes: `numpy`, `matplotlib`

Instalación rápida:

```bash
pip install numpy matplotlib
```


**Uso**
- Ejecutar el script:

```bash
python index.py
```

- El script imprimirá resultados por consola y abrirá dos gráficas (histograma y curva de probabilidad).

**Parámetros claves** (definidos al inicio de `index.py`):
- `N` : número total de estampas en el álbum (por defecto 100)
- `S` : estampas por sobre (por defecto 7)
- `R` : número de simulaciones (por defecto 10000)
- `M_values` : lista de valores de M evaluados en la Etapa 2

**Salida esperada**
- Estadísticas numéricas (media y desviación estándar de sobres y repetidas).
- Probabilidades de completar el álbum para distintos valores de M.
- Gráficas interactivas mostradas con `matplotlib`.

**Reproducibilidad**
- El script fija la semilla: `np.random.seed(2026)` para obtener resultados reproducibles.

**Notas**
- Para modificar el experimento, ajuste `N`, `S`, `R` o `M_values` en `index.py`.

**Autor**
- Marcela Castillo, Juan Rivas
