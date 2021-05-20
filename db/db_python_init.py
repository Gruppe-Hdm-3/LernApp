import mysql.connector as connector


user = """
    CREATE TABLE IF NOT EXISTS user (
        id SERIAL PRIMARY KEY,
        email VARCHAR(60) UNIQUE,
        first_name VARCHAR(60),
        last_name VARCHAR(60)
    )
"""

profile = """
    CREATE TABLE IF NOT EXISTS profile (
        id SERIAL PRIMARY KEY,
        user UNIQUE INTEGER,
        semester INTEGER,
        interests VARCHAR(240),
        type_ VARCHAR(30),
        online BOOL,
        frequency INTEGER,
        expertise VARCHAR(30),
        extroversion VARCHAR(30)
    )
"""


if __name__ == "__main__":
    connection_arguments = {
        "user": "root",
        "password": "mariadbpw",
        "host": "localhost",
        "database": "dummydb",
        "port": "33061"
    }
    cnx = connector.connect(**connection_arguments)
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(drop_person)
    cursor.execute(person)
