import streamlit as st
import time 

st.title("Media") 

st.header("Saiba Sua media a partir das suas 4 notas") 

soma = 0 

for i in range(1,5): 
    nota = st.number_input(f"Digite o {i}° nota: ", step=1.0)
    soma = soma + nota 
    
media = soma / 4 

if st.button("Saber Media"):
    st.success(f"A média é igual:{media}") 
else:
    st.info("Infome as notaas, BURRO!!!") 