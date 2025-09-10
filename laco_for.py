import streamlit as st
import time 

st.title("Laço de repetição - FOR") 

st.header("Contagem de 100 a 120.") 

numero = st.number_input("Digite um numero: ", step=1) 

if st.button("Iniciar. "): 
    for i in range(100,201,2):
        st.write(i) 
        time.sleep(1) 
    st.header("Fim") 
