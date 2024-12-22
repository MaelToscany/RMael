import streamlit as st 
#
# Cabecera del formulario
#
st.title('Proyecto	: Mi Primera Aplicacion en Streamlit')
st.title('Alumna	: Maria Elena Guevara')
#|
# Implementacion de Widgets Interactivos
#
edad 		= st.number_input('Edad', min_value=0, max_value=100, step=1) 
nomb_apell	= st.text_input('Nombres y Apellidos') 
mes 		= st.slider('Seleccionar Mes', min_value=1, max_value=12, step=1) 
acep_terms = st.checkbox('Acepta Terrminos y Condiciones') 
genero 		= st.radio('Genero', ('Masculino', 'Femenino', 'Otro')) 
pais 		= st.selectbox('Selecciona tu Pais', ['USA', 'Argentina', 'Peru','Colombia', 'Brasil', 'Chile',  'Ecuador', 'Uruguay' ,'Venezuela']) 
archivo 	= st.file_uploader('Cargar Archivo') 
fecha 		= st.date_input('Selecciona una Fecha') 
hora 		= st.time_input('Selecciona una Hora') 
#
# Guarda informacion ingresada
#
if st.button('Enviar Informacion'): 
	st.write('Edad:', edad) 
	st.write('Nombres y Apellidos:', nomb_apell) 
	st.write('Mes Seleccionado:', mes) 
	st.write('Acepta Terminos:', acep_terms) 
	st.write('Genero:', genero) 
	st.write('Pais:', pais) 
	st.write('Archivo Cargado:', archivo) 
	st.write('Fecha Seleccionada:', fecha) 
	st.write('Hora Seleccionada:', hora) 
# 
# revision de contenido en Barra Lateral 
#  
st.sidebar.title('Barra Lateral') 
st.sidebar.number_input('Edad (Sidebar)', min_value=0, max_value=100, step=1) 
st.sidebar.text_input('Nombres y Apellidos (Sidebar)') 
st.sidebar.slider('Seleccionar Mes (Sidebar)', min_value=1, max_value=12, step=1) 
st.sidebar.checkbox('Acepta Terminos (Sidebar)') 
st.sidebar.radio('Genero (Sidebar)', ('Masculino', 'Femenino', 'Otro')) 
st.sidebar.selectbox('Selecciona tu Pais (Sidebar)', ['USA', 'Argentina', 'Peru','Colombia', 'Brasil', 'Chile',  'Ecuador', 'Uruguay' ,'Venezuela'])
st.sidebar.file_uploader('Cargar Archivo (Sidebar)') 
st.sidebar.date_input('Selecciona una Fecha (Sidebar)') 
st.sidebar.time_input('Selecciona una Hora (Sidebar)')