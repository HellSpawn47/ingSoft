import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=ing-soft-etapa-3.database.windows.net;'
    'DATABASE=ing-soft-etapa-3;'
    'UID=administrador;'
)
cursor = conn.cursor()


def consulta_usuario(parametro_usuario):
    query = "SELECT * FROM Usuarios WHERE Nombre = '" + parametro_usuario + "'"
    cursor.execute(query)

    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)

consulta_usuario("Julian Jarazo")

cursor.close()
conn.close()
