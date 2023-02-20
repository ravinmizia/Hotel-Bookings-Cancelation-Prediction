import streamlit as st
import eda 
import prediction


navigation = st.sidebar.selectbox('Pilihan Halaman : ', ('Explore Data', 'Predict Cancelation'))


if navigation == 'Explore Data':
    eda.run()
else:
    prediction.run()
    
