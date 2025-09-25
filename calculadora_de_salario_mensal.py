import streamlit as st 
st.subheader ("Calculadora Salarial 💼")
st.title ("Calcule Seu Salario Mensal")

valor_hora = st.number_input("Digite quanto você ganha por hora: ", min_value=0.0)
hora = st.number_input  ("Digite quantas horas trabalhou no mês: ", min_value=0.0)
inss = st.number_input("Digite o desconto do INSS: ", min_value=0.0)

btn_calcular = st.button ("Calcular")

if btn_calcular:
    salario_bruto  = (valor_hora * hora)
    desconto_inss = salario_bruto * (inss / 100)
    salario_liquido = salario_bruto - desconto_inss


    st.write (f"💲O Seu Salario Liquido é De R$ {salario_liquido:.2f}")
