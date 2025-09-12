import streamlit as st
import time 

st.title("Media") 

st.header("Saiba Sua media a partir das suas 4 notas") 

soma = 0 

for i in range(1,4): 
    nota = st.number_input(f"Digite o {i}° nota: ", step=1.0)
    soma = soma + nota 
    
media = soma / 3



if st.button("Saber Media"):
    st.success(f"A média é igual:{media}") 
    if media >= 7:
        st.write("Aprovado")
    elif media <=6.9 and media >=4:
        st.write("Recu pae") 
    else:
        st.write("Reprovou kkkkkkkkkk") 
