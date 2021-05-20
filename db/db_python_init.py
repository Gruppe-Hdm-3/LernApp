import mysql.connector as connector


profile = """
    CREATE TABLE IF NOT EXISTS profile (
        id SERIAL PRIMARY KEY,
        owner INT,
        semester INTEGER,
        interests VARCHAR(240),
        type_ VARCHAR(30),
        online BOOL,
        frequence INTEGER,
        expertise VARCHAR(30),
        extroversion VARCHAR(30)
    )
"""


if __name__ == "__main__":
    connection_arguments = {
        "user": "root",
        "password": "Endgegner",
        "host": "localhost",
        "database": "mydb",
        "port": "3306"
    }
    cnx = connector.connect(**connection_arguments)
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(profile)