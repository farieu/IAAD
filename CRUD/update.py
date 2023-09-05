import streamlit as st
import mysql.connector
import pandas as pd

def build_header():
    st.markdown('<h1>Operações dinâmicas de Atualização para o BD Empresas 📲</h1>', unsafe_allow_html=True)
    st.markdown('<p>aaaaaaaaaaaaaaaa</p>', unsafe_allow_html=True)

def build_filter_controls(table_names):
    selected_table = st.radio("Selecione a tabela:", table_names)
    return selected_table

def build_update_form(selected_table, connection, cursor):
    st.write(f"Atualizar dados na tabela '{selected_table}':")

    cursor.execute(f"SHOW COLUMNS FROM {selected_table}")
    column_names = [column[0] for column in cursor.fetchall()]
    update_form = st.form(key='update_form')
    update_form.header("Formulário de Atualização")
    attribute_to_update = update_form.selectbox("Selecione um atributo para efetuar a atualização:", column_names)
    new_value = update_form.text_input(f"Novo valor a ser inserido:")
    where_clause = update_form.text_input("Clausúla WHERE (ex: id = 1):", help="Operadores AND e OR são permitidos.")

    if update_form.form_submit_button("Update"):
        update_query = f"UPDATE {selected_table} SET {attribute_to_update} = %s WHERE {where_clause}"
        cursor.execute(update_query, (new_value,))
        connection.commit()
        st.success("Atualização aplicada com sucesso!")

def main():
    build_header()
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="empresa_bd"
    )

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    table_names = [table[0] for table in cursor.fetchall()]
    selected_table = build_filter_controls(table_names)
    build_update_form(selected_table, connection, cursor)

if __name__ == "__main__":
    main()
