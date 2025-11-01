import streamlit as st
import time 

st.title("Laço de repetição - FOR") 

st.header("Tabuada do Netão") 

numero = st.number_input("Digite um número para saber a tabuada SEU BURRO",step=1)

if st.button("Iniciar. "): 
    for i in range(1, 10+1 , 1):
        resultado = numero * i 
        st.info(f'{numero} x {i} = {resultado}') 
        time.sleep(0.6) 
    st.success("Fim") 
