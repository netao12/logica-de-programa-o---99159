import streamlit as st 

st.title("login e senha") 

st.header("Coloque o login e senha") 

login_correto = "netinhopressao@gmail.com" 
senha_correto = "neto123" 


st.session_state.setdefault("campo", False) 
st.session_state.setdefault("tentativas", 0)

login = st.text_input("Insira seu login: ", disabled=st.session_state.campo)
senha = st.text_input("Digite a senha: ", type="password", disabled=st.session_state.campo) 

if st.button("Verificar"):
    if login == login_correto and senha ==  senha_correto:
        st.success("Dale ratão") 
    else: 
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:  
            st.warning(f"Não dale ratão, tentativas: {st.session_state.tentativas}") 
        else: 
            st.session_state.campo = True
            st.error("Número de tentativas inválida") 
