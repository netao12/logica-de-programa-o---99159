import streamlit as st 

st.title("Digite a Sua média") 

media = st.number_input("Digite a sua Média: ") 

if st.button("Verificar"): 
    if media >= 7:
        st.success("Aprovado") 
    else: 
        st.error("Reprovado") 
else:
    st.info("Digite a media, Por favor")  