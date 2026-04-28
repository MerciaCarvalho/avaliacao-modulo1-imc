import streamlit as st

st.title("calculadora 📱")
st.subheader("Feito com Streamlit ❤️")

altura = st.number_input("Digite a sua altura", min_value=0.0)
peso = st.number_input("Digite o seu peso" ,min_value=0.0)
  
if st.button("calcular"):
    imc = peso / altura ** 2
    st.success(f"seu IMC é {imc:.2f}")
    imc = peso / altura ** 2

    if imc < 18.5: 
        st.image ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_VlTQVI2Jy13D1wDh4hzxFrEN1Jl-cFVlOQ&s")
        st.error("Abaixo do peso")

    elif imc < 24.9:
        st.image ("https://i.pinimg.com/564x/33/0f/ff/330fffb3d3422820dc3b3591e5a90804.jpg")
        st.error ("Peso ideal")

    elif imc < 29.9:
        st.image ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsK9UkboLTRHP3fG-OwcyBbWaVCif0RWUNBA&s")
        st.error ("Sobrepeso")

    elif imc < 34.9:
        st.image ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdztqqrukU2RX97392v0dD-rrgo3_8TEMRiA&s")
        st.error ("Obesidade Grau I")

    elif imc < 39.9:
        st.image ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSV837PC0bU9SnQC3eyen0SZCuoyG_KY4Em4g&s")
        st.error ("Obesidade Grau II")
        
    elif imc > 40.0:
        st.image ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQ8eCzQeQ8WtIyFxjatu5VyOgmVGX6qdOhew&s")
        st.error ("Obesidade Grau III (mórbida)")
