import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('datasets/vehicles_us.csv')  # leer los datos
st.header('Streamlit Web App')

build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfica de dispersión')

if build_histogram:
    st.write(
        'Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creacion de una gráfica de dispersión para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
