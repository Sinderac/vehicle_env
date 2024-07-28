import streamlit as st
import plotly.express as px
import pandas as pd

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.title("Análisis de Datos de Vehículos")

# Sección de instrucciones y selección de gráfico
st.header("Selección de Gráfico")
graph_type = st.radio("Seleccione el tipo de gráfico:", ("Histograma", "Gráfica de Dispersión"))

if graph_type == "Histograma":
    st.write("Seleccione una columna para el eje X para construir un histograma.")

    # Selección de la columna para el histograma
    selected_column_hist = st.selectbox("Seleccione la columna para el eje X (Histograma)", car_data.columns.tolist())
    y_column_hist = st.selectbox("Seleccione la columna para el eje Y (Histograma)", car_data.columns.tolist())
        
    # Crear un botón para el histograma
    hist_button = st.button("Construir Histograma")

    if hist_button:
        # Mensaje de confirmación
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de carros')

        # Crear un histograma
        fig_hist = px.histogram(car_data, x=selected_column_hist, y= y_column_hist, title=f'Histograma de {selected_column_hist}')
        
        # Mostrar el gráfico
        st.plotly_chart(fig_hist, use_container_width=True)

elif graph_type == "Gráfica de Dispersión":
    st.write("Seleccione una columna para el eje X y una para el eje Y para construir una gráfica de dispersión.")

    # Selección de columnas para la gráfica de dispersión
    selected_column_scat = st.selectbox("Seleccione la columna para el eje X (Dispersión)", car_data.columns.tolist())
    y_column_scat = st.selectbox("Seleccione la columna para el eje Y (Dispersión)", car_data.columns.tolist())

    # Crear un botón para la gráfica de dispersión
    scat_button = st.button('Construir Gráfica de Dispersión')

    if scat_button:
        # Mensaje de confirmación
        st.write('Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de carros')

        # Crear una gráfica de dispersión
        fig_scat = px.scatter(car_data, x=selected_column_scat, y=y_column_scat, title=f'Gráfica de Dispersión de {y_column_scat} según {selected_column_scat}')
        
        # Mostrar el gráfico
        st.plotly_chart(fig_scat, use_container_width=True)

# Mostrar los datos en una tabla
st.subheader("Datos del Conjunto de Datos")
st.dataframe(car_data)