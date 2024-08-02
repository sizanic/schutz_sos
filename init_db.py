import sqlite3

connection = sqlite3.connect('database.db')

# Création des tables
with open('Documents\schema SCHUTZ.sql') as f:
    connection.executescript(f.read())
    connection.commit()

# ajout données initiales
with open('Documents\init_db_insert.sql') as f:
    connection.executescript(f.read())
    connection.commit()

connection.close()
