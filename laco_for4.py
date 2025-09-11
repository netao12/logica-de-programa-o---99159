import streamlit as st
import time 

st.title("Laço de repetição - FOR") 

st.header("Contagem Regressiva")  

numero = st.number_input("DIGITE O NUMERO", step=1) 

if st.button("Iniciar"): 
    for i in range(numero, 0, -1)
        st.write(i)
        time.sleep(0.60) 
    st.success("FIM")
else:
    st.warning("Digite o numero carambolas, macacos me mordam")