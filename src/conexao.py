import mysql
import mysql.connector


conn = mysql.connector.connect(
    username = "henrique",
    host = "localhost",
    password = "projeto123",
    db = "projeto_crud"
)

if conn.is_connected():
    print("Conectado com o banco")
else:
    print("Nao conectado com o banco")