import sqlite3

conn = sqlite3.connect("meubanco2.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Victor", "victor@exemplo.com"))
conn.commit()

cursor.execute("SELECT id, nome, email FROM usuarios")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}")

conn.close()
