# verifique a idade de um pessoa.
# se menor que 18, mostre: menor de idade.
# caso contráriio< mostre: maior de idade.
# usando stramlit. 

import streamlit as st 

st.title("Fala a idade painho") 

idade = st.number_input("digite sua idade: ")

if st.button("Verificar"): 
    if idade <18:
        st.write("Rala comédia, vou chamar sua mãe.", min_value=0, max_value=130, step=1)  
    else: 
        st.write("Acessa o site meu mano.") 
else: 
    st.warning("Por favor, digite a idade pow.")
