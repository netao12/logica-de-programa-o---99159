import streamlit as st 

st.title("Soma, Média, O Produto, Menor e Maior") 

primeiro_numero = st.number_input("Digite o primeiro número: ") 

segundo_numero = st.number_input("DIgite o segundo número: ") 

media = (primeiro_numero + segundo_numero) /2
produto = primeiro_numero * segundo_numero 

valor_maximo = max(primeiro_numero, segundo_numero) 
valor_minimo = min(primeiro_numero, segundo_numero)

if st.button("Rodar"): 

    st.write(f"a soma dos numeros é:{primeiro_numero + segundo_numero}") 
    st.write(f"a média é: {media}") 
    st.write(f"O produto é igual a:{produto}") 
    st.error(f"Menor número: {valor_minimo}")
    st.success(f"Maior número: {valor_maximo}") 
else: 
    st.info("informe os números. ") 