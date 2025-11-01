
import streamlit as st
import time
 
st.header("Ímpar e Par") 

st.write("Program de ímpar e par") 

pares = 0
ímpares = 0 

for i in range(1,5): 
    numero = st.number_input(f"Digite o {i}° número: ", step=1)
    if numero % 2 == 0:
        pares = pares + 1 
    else: 
        ímpares = ímpares + 1 

if st.button("Verificar"): 
    st.info(f"Quantidade de pares: {pares}")
    st.info(f"Quantidade de ímpares: {ímpares}") 