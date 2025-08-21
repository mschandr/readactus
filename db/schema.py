# db/schema.py
import mysql.connector
from mysql.connector import Error

def get_schema(db_fields):
    host = db_fields['host'].get()
    port = db_fields['port'].get()
    user = db_fields['user'].get()
    password = db_fields['password'].get()
    database = db_fields['database'].get()

    schema_output = []

    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for (table,) in tables:
            cursor.execute(f"SHOW CREATE TABLE `{table}`")
            create_stmt = cursor.fetchone()[1]
            schema_output.append(f"-- {table} --\n{create_stmt}\n")

        cursor.close()
        conn.close()

    except Error as e:
        schema_output.append(f"Error retrieving schema: {e}")

    return "\n\n".join(schema_output)

