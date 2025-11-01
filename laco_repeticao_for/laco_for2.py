import streamlit as st
import time 

st.title("Laço de repetição - FOR") 

st.header("Contagem de 1 a 20 (impar).") 

numero = st.number_input("Digite um numero: ", step=1) 

if st.button("Iniciar. "): 
    for i in range(1,21,2):
        st.write(i) 
        time.sleep(1) 
    st.success("Fim") 
