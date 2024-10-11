import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
import os 

# Carregando váriaveis do arquivo .env


# Configuração do banco de dados PostgreSQL
DB_HOST= 'dpg-cs02kujv2p9s73d2e5j0-a.oregon-postgres.render.com'
DB_NAME= 'dbname_ly4o'
DB_USER= 'postgresadmin'
DB_PASS= 'G3ODu39woq1Hj6aonGphKR2oq8tFL7PF'

'''DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")'''

# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host = DB_HOST,
            database = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )
        cursor = conn.cursor()

        # Inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s,%s,%s,%s,%s)"
        )
        cursor.execute(insert_query,(
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")