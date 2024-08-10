import streamlit as st
import pandas as pd

# Datos de ejemplo para el listado de consultas
data = {
    "ID": [1, 2, 3, 4],
    "Carátula": ["Juan Pérez", "Ana Gómez", "Luis Rodríguez", "María López"],
    "DNI": ["12345678", "23456789", "34567890", "45678901"],
    "Teléfono": ["111-1111", "222-2222", "333-3333", "444-4444"],
    "Fecha de Ingreso": ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04"],
    "Estado": ["Abierto", "Cerrado", "En Progreso", "Abierto"],
    "Equipo a Cargo": ["Equipo A", "Equipo B", "Equipo C", "Equipo A"],
    "Dependencia a Cargo": ["Dependencia 1", "Dependencia 2", "Dependencia 1", "Dependencia 3"],
}

# Convertir a un DataFrame de pandas
df = pd.DataFrame(data)
df = df.set_index("ID")

# Título centrado en la barra lateral
st.sidebar.markdown(
    """
    <h1 style="text-align: center;">DAJ</h1>
    """,
    unsafe_allow_html=True,
)

# Mostrar el logo de forma original en la barra lateral
st.sidebar.image("logo.png")

# Opciones de navegación con emojis
options = {
    "📋 Consultas": "Consultas",
    "🚨 Denuncias": "Denuncias",
    "📦 Requerimientos": "Requerimientos",
    "📅 Calendario": "Calendario",
    "📊 Estadísticas": "Estadísticas",
}

# Mostrar la lista de opciones en la barra lateral sin títulos adicionales
page = st.sidebar.selectbox("", options.keys())

# Contenido principal basado en la página seleccionada
if options[page] == "Consultas":
    st.title("Consultas")

    # Botón para cargar un nuevo caso alineado a la derecha
    st.markdown(
        """
        <div style="display: flex; justify-content: flex-end;">
            <button style="padding: 8px 16px; border-radius: 4px; background-color: #007bff; color: white; border: none; cursor: pointer;">
                Cargar nuevo caso
            </button>
        </div>
        """,
        unsafe_allow_html=True,
    )

    search_term = st.text_input("Buscar por nombre, apellido o DNI:")

    if search_term:
        filtered_df = df[
            df["Carátula"].str.contains(search_term, case=False) | df["DNI"].str.contains(search_term, case=False)]
    else:
        filtered_df = df

    # Mostrar la tabla con st.dataframe
    st.dataframe(filtered_df)

elif options[page] == "Denuncias":
    st.title("Denuncias")
    st.write("Página en desarrollo...")

elif options[page] == "Requerimientos":
    st.title("Requerimientos")
    st.write("Página en desarrollo...")

elif options[page] == "Calendario":
    st.title("Calendario")
    st.write("Página en desarrollo...")

elif options[page] == "Estadísticas":
    st.title("Estadísticas")
    st.write("Página en desarrollo...")
