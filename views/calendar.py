import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# DataFrame para guardar las reservas
reservas = pd.DataFrame(columns=["Fecha", "Reservado por", "Equipo"])

def show():
    st.title("Calendario")

    # Selector de fecha
    selected_date = st.date_input("Seleccione una fecha para agendar un turno", datetime.today())

    # Preguntar quién reserva
    reservado_por = st.text_input("¿Quién reserva?")

    # Selector de equipo
    equipo = st.selectbox("¿Con qué equipo es necesaria la gestión?", ["Equipo Jurídico", "Agencia Territorial", "Equipo Interdisciplinario"])

    # Botón para agendar el turno
    if st.button("Agendar turno"):
        if reservado_por:
            global reservas
            # Guardar la reserva en el DataFrame
            nueva_reserva = pd.DataFrame({
                "Fecha": [selected_date],
                "Reservado por": [reservado_por],
                "Equipo": [equipo]
            })
            reservas = pd.concat([reservas, nueva_reserva], ignore_index=True)
            st.success(f"Turno agendado para el {selected_date.strftime('%d/%m/%Y')} por {reservado_por} con el {equipo}.")
        else:
            st.error("Por favor, ingrese el nombre de la persona que reserva.")

    # Mostrar el calendario mensual con las fechas reservadas sombreadas
    st.subheader("Fechas Reservadas")
    if not reservas.empty:
        # Convertir las fechas a formato de texto
        reservas["Fecha"] = pd.to_datetime(reservas["Fecha"]).dt.strftime('%Y-%m-%d')

        # Mostrar calendario con fechas reservadas sombreadas
        dates_reserved = reservas["Fecha"].tolist()
        st.write("Fechas reservadas:", ", ".join(dates_reserved))

        # Mostrar las fechas reservadas en un calendario nivel mes
        st.write("Calendario de reservas:")
        for i in range(1, 32):
            day = selected_date.replace(day=i)
            if day.strftime('%Y-%m-%d') in dates_reserved:
                st.markdown(f"* **{day.strftime('%d/%m/%Y')}:** Reservado por {reservas[reservas['Fecha'] == day.strftime('%Y-%m-%d')]['Reservado por'].values[0]} con el {reservas[reservas['Fecha'] == day.strftime('%Y-%m-%d')]['Equipo'].values[0]}")
            else:
                st.markdown(f"{day.strftime('%d/%m/%Y')}: Disponible")
    else:
        st.write("No hay reservas aún.")

