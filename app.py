import streamlit as st
from  contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da compra", datetime.now()) # Data padrão 
    hora = st.time_input("Hora da compra", value=time(9,0)) # Horário padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produto", min_value=1, step=1)
    produto = st.selectbox(" Produto", options= ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])
    
    # Criando botão e aplicando funções para que ele mostra os resultados dos valores digitados na tela
    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)

            # venda Instanciando a minha classe
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro{e}")


if __name__ == "__main__":
    main = main()