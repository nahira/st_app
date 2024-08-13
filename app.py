import streamlit as st
import views.consultas
import views.denuncias
import views.requerimientos
import views.calendar
import views.estadisticas

# Mostrar el título "DAJ" con redirección a la página principal
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center;">
        <a href="?page=consultas" style="text-decoration: none; font-size: 2em; color: inherit;">
            <h1 style="margin: 0;">⚖️DAJ</h1>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Opciones de navegación con emojis
options = {
    "📋 Consultas": "consultas",
    "🚨 Denuncias": "denuncias",
    "📦 Requerimientos": "requerimientos",
    "📅 Calendario": "calendar",
    "📊 Estadísticas": "estadisticas",
}

# Mostrar la lista de opciones en la barra lateral
selected_page = st.sidebar.selectbox("", options.keys())

# Cargar la página seleccionada
if selected_page == "📋 Consultas":
    views.consultas.show()
elif selected_page == "🚨 Denuncias":
    views.denuncias.show()
elif selected_page == "📦 Requerimientos":
    views.requerimientos.show()
elif selected_page == "📅 Calendario":
    views.calendar.show()
elif selected_page == "📊 Estadísticas":
    views.estadisticas.show()
