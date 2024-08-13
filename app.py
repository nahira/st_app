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

# Mostrar el logo en su tamaño original con el texto "DAJ" al lado en la barra lateral
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center;">
        <img src="logo.png" style="margin-right: 10px;">
        <h1 style="margin: 0;">DAJ</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

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
    if st.button("Cargar nuevo caso"):
        with st.form("new_case_form"):
            st.write("Ingrese los detalles del nuevo caso:")
            caratula = st.text_input("Carátula (Nombre y Apellido)")
            dni = st.text_input("DNI")
            telefono = st.text_input("Teléfono")
            fecha_ingreso = st.date_input("Fecha de Ingreso")
            estado = st.selectbox("Estado", ["Abierto", "Cerrado", "En Progreso"])
            equipo_a_cargo = st.text_input("Equipo a Cargo")
            dependencia_a_cargo = st.text_input("Dependencia a Cargo")
            submit_button = st.form_submit_button(label="Guardar")

            if submit_button:
                # Agregar el nuevo registro al DataFrame
                new_id = df.index.max() + 1
                new_data = {
                    "ID": new_id,
                    "Carátula": caratula,
                    "DNI": dni,
                    "Teléfono": telefono,
                    "Fecha de Ingreso": fecha_ingreso,
                    "Estado": estado,
                    "Equipo a Cargo": equipo_a_cargo,
                    "Dependencia a Cargo": dependencia_a_cargo,
                }
                df = df.append(new_data, ignore_index=True)
                df = df.set_index("ID")
                st.success("Nuevo caso agregado exitosamente!")

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
