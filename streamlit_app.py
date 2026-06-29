"""
Dashboard — Desigualdad en Chile: Educación, Trabajo y Territorio (CASEN 2024)
Grupo 7 · Entregable 3 · Data Visualization

Layout EN CASCADA (un gráfico por fila). Muestra EXACTAMENTE las mismas 6 figuras
del informe A4 (los mismos PNG), con sus títulos y descripciones → "completamente
alineado con los gráficos del informe". No requiere el .dta de 1.6 GB.
Ejecutar:  streamlit run streamlit_app.py
"""
from pathlib import Path
import streamlit as st

DATA = Path(__file__).parent / "dashboard_data"
CORP = "#1e3a5f"

st.set_page_config(page_title="Desigualdad en Chile · CASEN 2024", page_icon="🇨🇱",
                   layout="centered")

# Los 6 paneles: MISMO PNG, título y descripción que el informe A4.
PANELS = [
    ("G1_INGRESO_REGION.png", "A) Ingreso mensual mediano por región",
     "Mediana de ingreso por región (CASEN 2024, adultos ≥25; mediana nacional $568k). "
     "Magallanes, la R. Metropolitana y Antofagasta encabezan; Ñuble y La Araucanía caen "
     "cerca de un 20% por debajo."),
    ("g2_std.png", "B) Brecha de ingresos respecto a la mediana nacional",
     "Desviación porcentual de la mediana de ingreso de cada región frente a la mediana nacional "
     "($568k, adultos ≥25). Azul: sobre la mediana; rojo: bajo. Magallanes lidera (+23%); Ñuble y "
     "La Araucanía caen cerca de un 20% por debajo."),
    ("g3_sankey_trayectorias.png", "C) Trayectorias: educación, sector e ingreso",
     "Flujo ponderado de trabajadores: educación › sector económico › tramo de ingreso. La "
     "educación superior es el puente casi exclusivo al quintil más alto (Q5)."),
    ("g5_std.png", "D) Evolución histórica de la brecha de ingresos Q5/Q1",
     "Razón de ingresos Q5/Q1: cayó de 12,7× (2006) a 8,6× (2024), −32%. Las barras muestran la "
     "variación anual (verde: baja, rojo: alza); el alza de 2020 coincide con la pandemia."),
    ("g5_heatmap_edu_quintil.png", "E) Retorno a la educación e ingresos individuales",
     "Distribución por quintil de ingreso dentro de cada nivel educativo (cada fila suma 100%). "
     "El 57% con postgrado está en Q5; la educación básica se concentra en Q1-Q2."),
    ("g6_final.png", "F) Radiografía del bienestar territorial (5D)",
     "Índice 0-10 por dimensión de bienestar. La RM lidera en sueldo, educación y salud, pero "
     "queda bajo el resto del país en seguridad y cohesión social."),
]

# ── Cabecera ────────────────────────────────────────────────────────────────
st.title("Desigualdad en Chile: Educación, Trabajo y Territorio")
st.caption("Un análisis multidimensional de las brechas de ingresos y el bienestar social · "
           "Encuesta CASEN 2024 · Grupo 7 · Entregable 4")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Mediana nacional", "$568k")
c2.metric("Región líder", "Magallanes", delta="+23,2% vs mediana")
c3.metric("Brecha Q5/Q1 (2024)", "8.6×", delta="−32% en 18 años", delta_color="inverse")
c4.metric("Postgrado en Q5", "57,2%")

st.sidebar.header("Navegación")
st.sidebar.markdown(
    "- **A** · Ingreso mediano por región\n"
    "- **B** · Brecha regional de ingresos\n"
    "- **C** · Trayectorias (Sankey)\n"
    "- **D** · Evolución Q5/Q1\n"
    "- **E** · Educación × ingreso\n"
    "- **F** · Bienestar territorial (radar)")
st.sidebar.info("N = 218.367 personas (CASEN 2024) · serie histórica 2006-2024.\n\n"
                "Las figuras son idénticas a las del informe A4 (mismos archivos).\n\n"
                "Fuente: Encuesta CASEN, Ministerio de Desarrollo Social y Familia.")

# ── Paneles en cascada (un gráfico por fila) ────────────────────────────────
for img, title, cap in PANELS:
    st.divider()
    st.subheader(title)
    st.image(str(DATA / img), use_container_width=True)
    st.caption(cap)

# ── Análisis ────────────────────────────────────────────────────────────────
st.divider()
st.subheader("Análisis e interpretación")
st.markdown(
    "Aunque la desigualdad de ingresos en Chile se ha reducido un **32% en 18 años**, el bienestar "
    "sigue condicionado por fracturas geográficas y educativas. Existe un marcado **centralismo "
    "económico**: la Región Metropolitana, junto con Magallanes y Antofagasta, supera la mediana "
    "nacional, mientras **Ñuble y La Araucanía caen cerca de un 20% por debajo**. Además, la RM "
    "concentra mayores ingresos, escolaridad y salud, pero queda por debajo del resto del país en "
    "seguridad y cohesión social. Finalmente, la **movilidad está dictada por la educación**: el "
    "postgrado es el puente casi exclusivo al quintil 5, mientras la educación básica relega a la "
    "población a la agricultura y a los quintiles de menores ingresos.")
