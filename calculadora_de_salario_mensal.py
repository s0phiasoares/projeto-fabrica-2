import streamlit as st 
st.subheader ("Calculadora Salarial 💼")
st.title ("Calcule Seu Salario Mensal")

valor_hora = float(input ("Digite quanto você ganha por hora: "))
hora = float (input ("Digite quantas horas trabalhou no mês: "))
inss = float (input("Digite o desconto do INSS: "))

btn_calcular = st.button ("Calcular")

salario_bruto  = (valor_hora * hora)
desconto_inss = salario_bruto * (inss / 100)
salario_liquido = salario_bruto - desconto_inss


print (f"💲O Seu Salario Liquido é De R$ {salario_bruto:.2f}")