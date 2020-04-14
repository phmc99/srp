import sqlite3

conn = sqlite3.connect('usersBd.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados >>> Users")