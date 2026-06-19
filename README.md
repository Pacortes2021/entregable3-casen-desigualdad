# Dashboard — Desigualdad en Chile (CASEN 2024) · Grupo 7-5

Dashboard de Streamlit en **cascada** (un gráfico por fila) que muestra **exactamente
las mismas 6 figuras del informe A4** (los mismos archivos PNG) → cumple el criterio
de la pauta "the dashboard is completely aligned with the plots provided in the report".

## Ejecutar localmente
```bash
python3 -m streamlit run streamlit_app.py
```
Se abre en http://localhost:8501

## Archivos necesarios (todos pequeños, sin el .dta)
- `streamlit_app.py` — la app (cascada de imágenes + cabecera, métricas y análisis)
- `requirements.txt` — solo `streamlit`
- `dashboard_data/` — las 6 figuras del informe:
  - `G1_INGRESO_REGION.png` (A) · `G1_SCATTER_REGION.png` (B)
  - `g3_sankey_trayectorias.png` (C) · `g5_std.png` (D)
  - `g5_heatmap_edu_quintil.png` (E) · `g6_final.png` (F)

> Estas figuras son **byte-idénticas** a las del informe (verificado por md5).
> Para regenerarlas: `build_a4_grid.py` / `build_pptx.py` y los scripts `_render_*.py`.

## Desplegar en Streamlit Cloud (para obtener el link de la pauta)
1. Subir a un repo de GitHub: `streamlit_app.py`, `requirements.txt` y la carpeta
   `dashboard_data/` (al menos los 6 PNG). **No** subir `casen_2024.dta`.
2. En https://share.streamlit.io → "New app" → elegir el repo y `streamlit_app.py`.
3. Copiar la URL pública resultante en el informe A4.
