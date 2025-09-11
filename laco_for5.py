import streamlit as st
import time

st.title("Laço de repetição - FOR") 

st.header("Soma de cinco números") 

st.write("Progtama de soma") 

soma=0

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}° número: ", step=1, min_value=0)
    soma = soma + numero
    time.sleep(1)

if st.button("Iniciar"): 
    st.success(f"A soma do número é:{soma}") 
else: 
    st.info("Informe um número")