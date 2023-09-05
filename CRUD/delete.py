import streamlit as st
import mysql.connector

def build_delete_form(selected_table, column_names, connection, cursor):
    st.write(f"Deletar dados na tabela '{selected_table}':")

    delete_option = st.selectbox("Selecione uma opção de exclusão:", ["Deletar registro com condição", "Deletar coluna", "Limpar tabela", "Deletar tabela"])

    if delete_option == "Deletar tabela":
        if st.checkbox("Confirmar exclusão da tabela"):
            cursor.execute(f"DROP TABLE {selected_table}")
            connection.commit()
            st.success(f"Tabela '{selected_table}' deletada com sucesso!")

    elif delete_option == "Deletar coluna":
        column_to_delete = st.selectbox("Selecione uma coluna para deleção:", column_names)
        if st.checkbox("Confirmar exclusão da coluna"):
            cursor.execute(f"ALTER TABLE {selected_table} DROP COLUMN {column_to_delete}")
            connection.commit()
            st.success(f"Coluna '{column_to_delete}' deletada com sucesso!")

    elif delete_option == "Deletar registro com condição":
        column_to_condition = st.selectbox("Selecione uma coluna para a condição:", column_names)
        where_value = st.text_input(f"Digite o valor para a condição na coluna '{column_to_condition}':", help="Cláusula WHERE")
        
        if st.button("Delete"):
            delete_query = f"DELETE FROM {selected_table} WHERE {column_to_condition} = %s"
            cursor.execute(delete_query, (where_value,))
            connection.commit()
            st.success("Exclusão aplicada com sucesso!")

    elif delete_option == "Limpar tabela":
        if st.checkbox("Confirmar exclusão de todos os valores da tabela"):
            cursor.execute(f"DELETE FROM {selected_table}")
            connection.commit()
            st.success(f"Todos os valores da tabela '{selected_table}' foram excluídos com sucesso!")

def main():
    st.markdown('<h1>Operações dinâmicas de Exclusão para o BD Empresas 📲</h1>', unsafe_allow_html=True)
    st.markdown('<p>Realização de operações CRUD no esquema Empresa. Para efetuar quaisquer deleções, é necessário especificar a operação de exclusão desejada, respeitando as regras de integridades advindad do esquema no MySQL. Para efetuar deleções específicas, utiliza-se o formado da clausula WHERE no <code>SQL.</code></p>', unsafe_allow_html=True)

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #Senha do teu MySQL
        database="empresa_bd"
    )

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    table_names = [table[0] for table in cursor.fetchall()]
    selected_table = st.radio("Selecione a tabela:", table_names)
    cursor.execute(f"SHOW COLUMNS FROM {selected_table}")
    column_names = [column[0] for column in cursor.fetchall()]

    build_delete_form(selected_table, column_names, connection, cursor)

if __name__ == "__main__":
    main()
