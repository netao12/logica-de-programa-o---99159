import streamlit as st 

st.title("laço de repetição - while") 

st.write("Algoritmo media") 

nota1= st.number_input("Digite a primeira nota: ", min_value=0, max_value=10)
nota2= st.number_input("Digite a segunda nota: ", min_value=0, max_value=10) 

media = (nota1 + nota2)/2

if st.button("Calcule média"): 
    st.info(f"média: {media}") 