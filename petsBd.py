import sqlite3

conn = sqlite3.connect('petsBd.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pets (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Tipo TEXT NOT NULL,
    Raca TEXT NOT NULL,
    Sexo TEXT NOT NULL,
    NomeDono TEXT NOT NULL,
    TelDono INTEGER NOT NULL
);
""")

print("Conectado ao Banco de Dados >>> Pets")