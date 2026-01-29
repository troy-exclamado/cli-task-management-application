import mysql.connector
from database import DB_CONFIG

def run_migrate():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    with open("migrations/task_table.sql", "r") as file:
        sql_script = file.read()

    statements = sql_script.split(";")

    for stmt in statements:
        stmt = stmt.strip()
        if stmt: 
            cursor.execute(stmt)

    conn.commit()
    cursor.close()
    conn.close()

    print("Database migration completed.")

if __name__ == "__main__":
    run_migrate()