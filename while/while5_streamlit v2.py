import streamlit as st 

st.title("login e senha") 

st.header("Coloque o login e senha") 

login_correto = "netinhopressao@gmail.com" 
senha_correto = "neto123" 

tentivas = 0

login = st.text_input("Insira seu login: ")
senha = st.text_input("Digite a senha:", type="password") 

if st.button("Verificar"):
    if login == login_correto and senha ==  senha_correto:
        st.success("Dale ratão") 
    else: 
        st.error("Não dale ratão") 


if tentivas > 3: 
    print("programa encerrado")