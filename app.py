import streamlit as st
import calculadora as calc



st.title("Calculadora ☆*: .｡. o(≧▽≦)o .｡.:*☆")

numero1 = st.number_input("digite o primeiro número: ", step=0.1, value=None )
numero2 = st.number_input("digite o segundo número: ", step=0.1, value=None)
operacao = st.selectbox("selecione a operação",["+","/","*","-"])
if st.button("calcular"):
    resultado = calc.calcular(numero1,numero2, operacao)
    st.info(f"o resultado é: {resultado}")
    if resultado == 67:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuEzzh4Pf0VryPpj_malmSdwstzEU-eWlfgg&s")